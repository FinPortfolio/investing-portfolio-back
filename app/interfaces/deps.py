from adapters.db.session import get_session
from adapters.db.repositories.user_repository_impl import SQLAlchemyUserRepository
from application.services.user_service import UserService

def get_user_service():
    session = next(get_session())
    repo = SQLAlchemyUserRepository(session)
    return UserService(repo)
