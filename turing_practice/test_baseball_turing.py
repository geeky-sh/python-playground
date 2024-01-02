import pytest

def callPoints(ops) -> int:
    scores = []

    for op in ops:
        if op == "+":
            score = scores[-1] + scores[-2]
            scores.append(score)
        elif op == "D":
            score = scores[-1] * 2
            scores.append(score)
        elif op == "C":
            scores = scores[:-1]
        else:
            scores.append(int(op))

    return sum(scores)

@pytest.mark.parametrize("inp,expected", [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1"], 1)
    ])
def test_callPoints(inp, expected):
    assert callPoints(inp) == expected
