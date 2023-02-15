from infra.database.configs.engine import engine_factory
from sqlalchemy.orm import sessionmaker

engine = engine_factory()

DEFAULT_SESSION_MAKER = sessionmaker(bind=engine, expire_on_commit=True)