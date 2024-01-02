import pytest

"""
https://leetcode.com/problems/decode-ways/description/
"""

def numDecodings(s: str) -> int:
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        if s[0] == "0":
            return 0
        else:
            return 1
    else:
        ans = 0
        e = s[-1:]
        if e != "0":
            ans += numDecodings(s[:-1])

        e = s[-2:]
        if not e.startswith('0') and int(e) <= 26:
            if len(s) == 2:
                ans += 1
            else:
                ans += numDecodings(s[:-2])
        return ans


@pytest.mark.parametrize("inp,expected", [
    ("11106", 2),
    ("12", 2),
    ("226", 3),
    ("06", 0)
])
def test_numDecodings(inp, expected):
    assert numDecodings(inp) == expected
