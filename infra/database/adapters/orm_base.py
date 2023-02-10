from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import func


class BaseTable(DeclarativeBase):
    created_when: Mapped[datetime] = mapped_column(default=func.now())
    modified_when: Mapped[datetime] = mapped_column(default=func.now())