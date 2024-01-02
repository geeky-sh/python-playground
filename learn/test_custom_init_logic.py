from typing import Self
import pytest

class PlayerLimitException(Exception):
    pass

class Player:
    total = 0

    def __new__(cls, name) -> Self:
        if cls.total == 11:
            raise PlayerLimitException("You cannot add more than 11 players")

        cls.total += 1
        return super().__new__(cls)

    def __init__(self, name) -> None:
        self.name = name


def test_custom_init_logic():
    for i in range(11):
        name = "name-{}".format(i)

        Player(name=name)

    assert Player.total == 11, "Total no. of players should be 11 by now"

    with pytest.raises(PlayerLimitException) as exc:
        Player("name-12")

    assert str(exc.value) == "You cannot add more than 11 players"
