from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from tracker.models.base_model import BaseModel


@dataclass
class Expense(BaseModel):
    expense_id: UUID
    description: str
    value: Decimal
    due_date: date

    @classmethod
    def new_expense(cls, data: dict):
        return cls(
            expense_id=cls.expense_id,
            description=cls.description,
            value=cls.value,
            due_date=cls.due_date,
        )
