import pytest

def add(a: int, /, b: int) -> int:
    return a + b

def test_only_positional():
    assert add(8, 2) == 10, "Incorrect Answer"
    assert add(8, b=12), "See how positional arguments are placed"

    with pytest.raises(TypeError) as exc:
        add(a=8, b=12)

    assert str(exc.value) == "add() got some positional-only arguments passed as keyword arguments: 'a'"
