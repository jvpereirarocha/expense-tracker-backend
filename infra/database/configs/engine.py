from sqlalchemy import create_engine
from os import getenv


def engine_factory():
    return create_engine(
        url=getenv("DATABASE_URI")
    )