from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.adapters.db.models import Base
from main import main_app
from app.adapters.db import pg_db_manager
from core.config import settings


def pytest_collection_modifyitems(items):
    """
    Adds the loop_scope="session" parameter to the decorator for all tests.
    Details: https://github.com/pytest-dev/pytest-asyncio/issues/922
    """
    pytest_asyncio_tests = (item for item in items if pytest_asyncio.is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope='session')
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)


@pytest.fixture
def test_db():
    """
    Fixture for setting up a test database.

    - Uses environment variables from `.env` for configuration;
    - Creates an asynchronous SQLAlchemy engine and session;
    - Ensures that all tables are created and dropped before and after tests;
    - Ensures that each test session starts with a clean database.

    Returns:
        init_db (Callable): Coroutine for creating all tables;
        drop_db (Callable): Coroutine to delete all tables.
    """

    database_url = str(settings.db.url)
    engine = create_async_engine(database_url, echo=False, poolclass=NullPool)
    TestingSessionLocal = async_sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False, autocommit=False
    )

    async def init_db():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_db():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        await engine.dispose()

    pytest.db_engine = engine
    pytest.db_sessionmaker = TestingSessionLocal

    return init_db, drop_db


@pytest_asyncio.fixture
async def async_session(test_db) -> AsyncGenerator[AsyncSession, None]:
    """
    Fixture for creating an asynchronous database session before each test.

    - Before testing, resets the database, creating a clean test environment;
    - Opens a new session for testing;
    - After the test, automatically executes `rollback()` and closes the session.

    Returns:
        AsyncSession: SQLAlchemy asynchronous session object.
    """
    init_db, drop_db = test_db
    await drop_db()
    await init_db()

    session = pytest.db_sessionmaker()
    try:
        yield session
    finally:
        await session.rollback()
        await session.close()


@pytest_asyncio.fixture
async def client(async_session):
    """
    Fixture for creating a FastAPI test client.

    - Overrides the `get_async_session` dependency so that tests use the test DB;
    - Creates an `AsyncClient` with an `ASGITransport`, emulating HTTP requests;
    - Automatically cleans up `dependency_overrides` after tests complete.

    Returns:
        AsyncClient: Asynchronous client for API testing.
    """

    async def override_get_async_session():
        async with async_session as session:
            try:
                yield session
            finally:
                await session.rollback()
                await session.close()
    main_app.dependency_overrides[pg_db_manager.session_getter] = override_get_async_session

    async with AsyncClient(transport=ASGITransport(main_app), base_url="http://test") as ac:
        try:
            yield ac
        finally:
            await ac.aclose()
            main_app.dependency_overrides.clear()