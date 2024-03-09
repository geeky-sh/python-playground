import pytest
import math

class Solution(object):
    def isPeak(self, idx, size, nums):
        v = nums[idx]
        l = -math.inf
        h = -math.inf

        if idx > 0:
            l = nums[idx-1]
        if idx < size-1:
            h = nums[idx+1]

        if l < v and v > h:
            return True
        return False


    def peakIdx(self, low, high, size, nums):
        if low > high or low < 0 or high >= size:
            return -1

        s = high + low
        mid = int(s / 2)
        if self.isPeak(mid, size, nums):
            return mid

        res = self.peakIdx(low, mid - 1, size, nums)
        if res != -1:
            return res

        return self.peakIdx(mid + 1, high, size, nums)



    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        do a binary search and get its peak
        """
        sz = len(nums)
        return self.peakIdx(0, sz - 1, sz, nums)



@pytest.mark.parametrize("nums,exp", [
    ([1,2,3,1],2),
    ([1,2,1,3,5,6,4],1)
])
def test_peak_func(nums, exp):
    assert Solution().findPeakElement(nums) == exp
