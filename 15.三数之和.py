#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # result = []
        # if len(nums)<3:
        #     return result
        # for i in range(len(nums)):
        #     if i == len(nums)-2:
        #         break
        #     first_value = nums[i]
        #     for j in range(i+1, len(nums)):
        #         second_value = nums[j]
        #         for z in range(j+1, len(nums)):
        #             third_value = nums[z]
        #             if (first_value+second_value+third_value) == 0:
        #                 three_value_sum = [first_value, second_value, third_value]
        #                 if three_value_sum not in result:
        #                     result.append([first_value, second_value, third_value])

        # return result
        n = len(nums)
        nums.sort()
        ans = list()
        
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            third = n - 1
            for second in range(first+1, n):
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                while second < third and (nums[second] + nums[third]) > target:
                    third -= 1
                if second == third:
                    break 
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans
# @lc code=end
solution = Solution()

print(solution.threeSum([-1, 0, 1, 2,-1, 4]))
