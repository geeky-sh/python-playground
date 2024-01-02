import pytest

def isValid(s: str) -> bool:
    stk = []
    try:
        for ch in s:
            if ch == "}":
                pre = stk.pop()
                if pre != "{":
                    return False
            elif ch == ")":
                pre = stk.pop()
                if pre != "(":
                    return False
            elif ch == "]":
                pre = stk.pop()
                if pre != "[":
                    return False
            else:
                stk.append(ch)
    except IndexError:
        return False
    return len(stk) == 0


@pytest.mark.parametrize("inp,expected", [
    ("()", True),
    ("()[]{}", True),
    ("[)", False),
    ("[(]]]]", False)
])
def test_isValid(inp, expected):
    assert isValid(inp) == expected
