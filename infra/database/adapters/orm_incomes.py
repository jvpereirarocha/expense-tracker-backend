from datetime import date
from decimal import Decimal
from uuid import UUID, uuid4
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from infra.database.adapters.orm_base import BaseTable


class IncomeTable(BaseTable):
    __tablename__ = "incomes"

    income_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4().hex, unique=True)
    description: Mapped[str] = mapped_column(String(255))
    value: Mapped[Decimal]
    receivment_date: Mapped[date]
    monthly_received: Mapped[bool] = mapped_column(Boolean, default=False)