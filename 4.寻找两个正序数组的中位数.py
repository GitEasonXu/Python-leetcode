#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sum_nums = nums1 + nums2
        sum_nums.sort()
        sum_nums_len = len(sum_nums)
        if sum_nums_len == 0:
            return 0.0
        elif sum_nums_len == 1:
            return sum_nums[0]
        elif sum_nums_len % 2 == 0:
            midd_index = int(sum_nums_len // 2)
            return (sum_nums[midd_index] + sum_nums[midd_index-1]) / 2.0
        elif sum_nums_len % 2 == 1:
            midd_index = int(sum_nums_len // 2)
            return sum_nums[midd_index]
# @lc code=end

