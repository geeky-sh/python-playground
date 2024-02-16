from typing import Self
from .domains import Borrower, User, Expense
from dataclasses import dataclass

from .repositories import UserRepo, BorrowRepo, ExpenseRepo


@dataclass
class Engine:
    user_repo: UserRepo
    borrower_repo: BorrowRepo
    expense_repo: ExpenseRepo

    def process_expense(self, expense_str: str):
        tokens = expense_str.split(" ")

        user_id = tokens[0]
        amount = int(tokens[1])
        among_users = []
        among_amounts = []

        count = 2
        for token in tokens[2:]:
            if token in ['EXACT', 'EQUAL', 'PERCENT']:
                break
            among_users.append(token)
            count +=1

        if token == 'EQUAL':
            among_amounts = [amount / 4]*4
        elif token == 'EXACT':
            among_amounts = tokens[count:]
        elif token == 'PERCENT':
            for tk in tokens[count:]:
                ag = (int(tk)*amount) / 100
                among_amounts.append(ag)


        expense = self.expense_repo.add(user_id=user_id, amount=amount, among_users=among_users, among_amounts=among_amounts)
        self.borrower_repo.create_from_expense(expense=expense)

    def show_borrows(self, user_str: str):
        borrows = []
        if user_str == "":
            borrows = self.borrower_repo.get_all_borrows()
        else:
            user = self.user_repo.get(user_str.strip())
            borrows = self.borrower_repo.get_borrows_for_user(user=user)

        for borrow in borrows:
            print(borrow)

if __name__ == "__main__":
    u1 = User(name="User 1", id="u1")
    u2 = User(name="User 2", id="u2")
    u3 = User(name="User 3", id="u3")
    u4 = User(name="User 4", id="u4")

    user_repo = UserRepo.build(users=[u1, u2, u3, u4])
    expense_repo = ExpenseRepo.build()
    borrow_repo = BorrowRepo.build()

    engine = Engine(user_repo=user_repo, expense_repo=expense_repo, borrower_repo=borrow_repo)
    with open("input.txt") as f:
        line = f.readline()
        if line.startswith('SHOW'):
            inp = line.replace(line, "SHOW", "").strip()
            engine.show_borrows(inp)
        if line.startswith("EXPENSE"):
            inp = line.replace("EXPENSE", "").strip()
            engine.process_expense(expense_str=inp)
