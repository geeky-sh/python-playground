from dataclasses import dataclass
from typing import List, Self
from .user import User

@dataclass
class Borrower:
    frm: User
    by: User
    amount: str

    def __eq__(self, __value: Self) -> bool:
        return self.frm == __value.frm and self.by == __value.by

    def repr(self, fr: str) -> str:
        "{} owes {}: {}".format(self.by.name, self.frm.name, self.amount)

    def is_opposite(self, value: Self) -> bool:
        return self.frm == value.by and self.by == value.frm
