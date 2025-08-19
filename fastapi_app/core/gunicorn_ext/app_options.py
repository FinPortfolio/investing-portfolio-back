from .logger import GunicornLogger


def get_app_options(
    workers: int,
    host: str,
    port: int,
    timeout: int,
    # log_level: str,
) -> dict:
    return {
        "worker_class": "uvicorn.workers.UvicornWorker",
        "workers": workers,
        "bind": f"{host}:{port}",
        "timeout": timeout,
        # "accesslog": "-",
        # "errorlog": "-",
        # "loglevel": log_level,
        # "logger_class": GunicornLogger,
    }
