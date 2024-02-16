from dataclasses import dataclass
from typing import List, Self

@dataclass
class ShareUser:
    amount: int
    user_id: int

@dataclass
class Expense:
    user_id: int
    amount: int
    operation: str # percent, exact, equal
    among_users: List[ShareUser]
