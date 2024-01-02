import pytest
from typing import List

def grayCode(n: int) -> List[int]:
        results = []
        visited = {}

        num = list("0"*n)
        snum = "".join(num)
        results.append(int(snum, 2))
        visited[snum] = 1
        size = 2 ** n

        while len(results) < size:
            for i, n in enumerate(num):
                if n == "0":
                    num[i] = "1"
                    snum = "".join(num)
                    if snum not in visited:
                        results.append(int(snum, 2))
                        visited[snum] = 1
                        break
                    num[i] = "0"
                else:
                    num[i] = "0"
                    snum = "".join(num)
                    if snum not in visited:
                        results.append(int(snum, 2))
                        visited[snum] = 1
                        break
                    num[i] = "1"

        return results

@pytest.mark.parametrize("inp,expected", [
     (2, [0, 2, 3, 1]),
     (1, [0, 1])
])
def test_grayCode(inp, expected):
     assert grayCode(inp) == expected
