from pathlib import Path

SUPPORTED_COUNTRY = ['CM']
TORTOISE_ORM = {
    "connections": {"default": "sqlite://src/.local_settings/database.sqlite3"},  # Example for SQLite
    "apps": {
        "models": {
            "models": ['api.database.modles'],  # Path to your Tortoise models
            "default_connection": "default",
        },
    },
}