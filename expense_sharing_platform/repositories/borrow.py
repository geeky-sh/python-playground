from typing import List, Self
from ..domains import Borrower, User, Expense
from .user import UserRepo

class BorrowRepo:
    borrows: List[Borrower]

    @classmethod
    def build(cls) -> Self:
        return cls(users=[])

    def create_from_expense(self, expense: Expense) -> None:
        for share_user in expense.among_users:
            user = UserRepo.get(uid=share_user.user_id)
            borrow = Borrower(frm=expense.user, by=user, amount=expense.amount)

            self.add(borrow=borrow)


    def add(self, borrow: Borrower):
        """
        if same found, append to it
        if opposite found, rehash it
        """
        new_borrow = None
        sim_borrow = self.get_sim_borrow(borrow=borrow)
        if sim_borrow:
            new_amount = sim_borrow.amount + borrow.amount
            new_borrow = Borrower(frm=sim_borrow.frm, by=sim_borrow.by, amount=new_amount)
            self.remove(sim_borrow)
            self.borrows.append(new_borrow)
            return

        opp_borrow = self.get_opp_borrow(borrow)
        if opp_borrow:
            if opp_borrow.amount > borrow.amount:
                new_amount = opp_borrow.amount - borrow.amount
                new_borrow = Borrower(frm=opp_borrow.frm, by=opp_borrow.by, amount=new_amount)
                self.remove(opp_borrow)
                self.borrows.append(new_borrow)
                return
            elif opp_borrow.amount < borrow.amount:
                new_amount = borrow.amount - opp_borrow.amount
                new_borrow = Borrower(frm=borrow.frm, by=borrow.by, amount=new_amount)
                self.remove(opp_borrow)
                self.borrows.append(new_borrow)
                return
            elif opp_borrow.amount == borrow.amount:
                self.remove(opp_borrow)
                return

        self.borrows.append(borrow)


    def remove(self, borrow):
        self.borrows = [b for b in self.borrows if not b == borrow]

    def get_all_borrows(self) -> List[Self]:
        return self.borrows

    def get_borrows_for_user(self, user: User) -> List[Self]:
        return [b for b in self.borrows if b.frm.id == user.id or b.by.id == user.id]

    def get_sim_borrow(self, borrow: Borrower):
        for sim_borrow in self.borrows:
            if borrow == sim_borrow:
                return sim_borrow

    def get_opp_borrow(self, borrow: Borrower):
        for opp_borrow in self.borrows:
            if opp_borrow.is_opposite(borrow):
                return opp_borrow
