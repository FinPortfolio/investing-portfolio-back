from fastapi import FastAPI
from gunicorn.app.base import BaseApplication


class GunicornFastAPIApp(BaseApplication):
    def __init__(
        self,
        application: FastAPI,
        options: dict,
    ):
        self.options = options
        self.application = application
        super().__init__()

    def load(self):
        return self.application

    @property
    def normalized_options(self) -> dict:
        return {
            # pair
            k: v
            # for each option
            for k, v in self.options.items()
            # not empty key / value
            if k in self.cfg.settings and v is not None
        }

    def load_config(self):
        for key, value in self.normalized_options.items():
            self.cfg.set(key.lower(), value)
