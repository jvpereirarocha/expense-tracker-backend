from sqlalchemy.orm import registry

from infra.database.adapters.orm_expenses import ExpenseTable
from tracker.models.expenses import Expense

register = registry()

def start_mappers():
    register.map_imperatively(Expense, ExpenseTable)