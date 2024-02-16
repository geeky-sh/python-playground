from typing import Self
from dataclasses import dataclass

@dataclass
class User:
    name: str
    id: str

    def __eq__(self, __value: Self) -> bool:
        return self.id == __value.id
