from itertools import combinations


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        may = combinations(nums, 2)
        for one in may:
            if sum(one) == target:
                result.append(nums.index(one[0]))
                result.append(nums.index(one[1]))
                return result
