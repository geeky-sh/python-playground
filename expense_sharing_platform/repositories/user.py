from typing import List, Self
from ..domains import User

class UserRepo:
    users: List[User]

    @classmethod
    def build(cls, users) -> Self:
        return cls(users=users)

    def add(self, uid, name):
        user = User(id=uid, name=name)
        self.users.append(user)

    def get(self, uid) -> User:
        for user in self.users:
            if user.id == uid:
                return user
