from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from tracker.models.base_model import BaseModel


@dataclass
class Income(BaseModel):
    income_id: UUID
    description: str
    value: Decimal
    receivment_date: date
    montly_received: bool

    @classmethod
    def new_income(cls, data: dict):
        return cls(
            income_id=cls.income_id,
            description=cls.description,
            value=cls.value,
            receivment_date=cls.receivment_date,
            monthly_received=cls.montly_received,
        )
