#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if len(intervals) <=1:
        #     return intervals
        # next_try = True
        # intervals.sort()
        # while next_try:
        #     change_flag = False
        #     for i in range(len(intervals)):
        #         if i + 1 == len(intervals):
        #             break
        #         block1_start_value = intervals[i][0]
        #         block1_end_value = intervals[i][1]
                
        #         block2_start_value = intervals[i+1][0]
        #         block2_end_value = intervals[i+1][1]


        #         if block2_start_value in range(block1_start_value, block1_end_value+1):
        #             if block2_end_value > block1_end_value:
        #                 intervals[i] = [block1_start_value, block2_end_value]
        #             intervals.pop(i+1)
        #             change_flag = True
        #             break
        #                 #intervals[i+1] = intervals[i]
        #     if change_flag:
        #         next_try = True
        #     else:
        #         next_try = False
        # return intervals

        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# @lc code=end

solution = Solution()
result = solution.merge([[0,0],[1,4]])
print(result)