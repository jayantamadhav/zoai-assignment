import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

DATABASE_URL = f"{os.getenv('DB_DIALECT')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models.booking", "app.models.hotel", "app.models.rating", "app.models.user"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["models.booking", "models.hotel", "models.rating", "models.user"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
