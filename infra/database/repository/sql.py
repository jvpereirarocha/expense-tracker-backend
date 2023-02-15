from typing import Iterable
from infra.database.configs import DEFAULT_SESSION_MAKER
from tracker.models.base_model import BaseModel
from tracker.services.abstract_repo import AbstractRepository


class SQLAlchemyRepo(AbstractRepository):
    def get_all(self) -> Iterable[BaseModel]:
        return super().get_all()