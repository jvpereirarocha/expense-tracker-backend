from datetime import date
from decimal import Decimal
from uuid import UUID, uuid4
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from infra.database.adapters.orm_base import BaseTable


class ExpenseTable(BaseTable):
    __tablename__ = "expenses"

    expense_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4().hex, unique=True)
    description: Mapped[str] = mapped_column(String(255))
    value: Mapped[Decimal]
    due_date: Mapped[date]