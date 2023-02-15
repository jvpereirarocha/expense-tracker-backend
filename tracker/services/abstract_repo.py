from abc import ABC, abstractmethod
from typing import Iterable, NoReturn

from uuid import UUID

from tracker.models.base_model import BaseModel


class AbstractRepository(ABC):
    @abstractmethod
    def get_one(self, entity_id: UUID) -> BaseModel:
        raise NotImplementedError()
    
    @abstractmethod
    def get_all(self) -> Iterable[BaseModel]:
        raise NotImplementedError()
    
    @abstractmethod
    def save_one(self, entity: BaseModel) -> NoReturn:
        raise NotImplementedError()