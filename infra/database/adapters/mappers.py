from sqlalchemy.orm import registry

from infra.database.adapters.orm_expenses import ExpenseTable
from infra.database.adapters.orm_incomes import IncomeTable
from tracker.models.expenses import Expense
from tracker.models.incomes import Income

register = registry()

def start_mappers():
    register.map_imperatively(Expense, ExpenseTable)
    register.map_imperatively(Income, IncomeTable)