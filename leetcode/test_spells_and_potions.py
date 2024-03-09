import pytest

class Solution(object):
    def findPortionIdx(self, val, low, high, size, potions, success):
        print(low, high)
        if low < 0 or high >= size or low > high:
            return -1

        hf = int((high + low) / 2)
        pd = potions[hf] * val
        if pd >= success:
            if hf == 0 or potions[hf-1]*val < success:
                return hf

            return self.findPortionIdx(val, low, hf-1, size, potions, success)
        elif pd < success:
            if hf < size-1 and potions[hf+1]*val >= success:
                return hf+1

            return self.findPortionIdx(val, hf + 1, high, size, potions, success)



    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        sz = len(potions)
        sp = []
        potions.sort()
        for s in spells:
            idx = self.findPortionIdx(s, 0, sz-1, sz, potions, success)
            if idx == -1:
                sp.append(0)
            else:
                sp.append(sz - idx)
        return sp

@pytest.mark.parametrize("spells,potions,success,expected", [
    # ([5,1,3],[1,2,3,4,5],7,[4,0,3]),
    # ([3,1,2],[8,5,8],16,[2,0,2]),
    ([15,8,19],[38,36,23],328,[3,0,3])
])
def test_successful_pairs(spells, potions, success, expected):
    assert Solution().successfulPairs(spells, potions, success) == expected
