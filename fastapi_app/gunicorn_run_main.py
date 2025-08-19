__all__ = (
    "main_app",
    "main",
)

from core.config import settings
from core.gunicorn_ext import get_app_options, GunicornFastAPIApp
from main import main_app


def main():
    gunicorn_app = GunicornFastAPIApp(
        application=main_app,
        options=get_app_options(
            workers=settings.gunicorn.workers,
            host=settings.gunicorn.host,
            port=settings.gunicorn.port,
            timeout=settings.gunicorn.timeout,
        )
    )
    return gunicorn_app.run()


if __name__ == "__main__":
    main()
