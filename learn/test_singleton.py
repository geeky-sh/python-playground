from typing import Self

class Singleton:
    instance = None

    def __new__(cls) -> Self:
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

def test_singleton():
    o1 = Singleton()
    o2 = Singleton()

    assert id(o1) == id(o2), "This is a Singleton class"
