import pytest
from .solution import get_calibration_value

# def get_calibration_value(word: str) -> int:
#     i = 0
#     j = len(word)-1

#     while not word[i].isdigit():
#         i += 1

#     while not word[j].isdigit():
#         j -= 1

#     return int("{}{}".format(word[i], word[j]))



@pytest.mark.parametrize("inp,expected", [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77)
])
def test_calibration_value(inp, expected):
    assert get_calibration_value(inp) == expected
