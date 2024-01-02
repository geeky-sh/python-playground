import pytest
from .solution import get_proper_calibration_value

# WORD_MAP = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5,
#     "six": 6,
#     "seven": 7,
#     "eight": 8,
#     "nine": 9
# }

# def get_proper_calibration_value(word: str) -> int:
#     first = 0
#     i = 0
#     while True:
#         if word[i].isdigit():
#             first = int(word[i])
#             break

#         if len(word[:i+1]) >= 3:
#             for w in WORD_MAP:
#                 if word[:i+1].endswith(w):
#                     first = WORD_MAP[w]
#                     break
#             if first:
#                 break

#         i += 1

#     second = 0
#     j = len(word)-1
#     while True:
#         if word[j].isdigit():
#             second = int(word[j])
#             break

#         if len(word[j:]) >= 3:
#             for w in WORD_MAP:
#                 if word[j:].startswith(w):
#                     second = WORD_MAP[w]
#                     break

#             if second:
#                 break


#         j -= 1

#     return int("{}{}".format(first, second))

@pytest.mark.parametrize("inp,expected", [
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz",13),
    ("xtwone3four",24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
])
def test_proper_calibration_value(inp, expected):
    assert get_proper_calibration_value(inp) == expected
