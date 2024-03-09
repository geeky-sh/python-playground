import pytest
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass


@pytest.mark.parametrize("piles,h,exp", [
    ([3,6,7,11],8,4),
])
def test_eating_speed(piles, h, exp):
    assert Solution().minEatingSpeed(piles, h) == exp
