from typing import List, Self
from ..domains import Expense, ShareUser

class ExpenseRepo:
    expenses: List[Expense]

    @classmethod
    def build(cls) -> Self:
        return cls(users=[])

    def add(self, user_id: str, amount: int, among_users: List[str], among_amounts: List[str]) -> Expense:
        among_user_objects = []
        for among_user_id, i in enumerate(among_users):
            among_user_objects.append(
                ShareUser(amount=among_amounts[i], user_id=among_user_id)
            )
        expense = Expense(user_id=user_id, amount=amount, among_users=among_user_objects)
        self.expenses.append(expense)
        return expense
