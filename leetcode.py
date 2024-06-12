# class Solution:
#     def twoSum(self, nums, target):
#         dic = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in dic:
#                 return [dic[complement], i]
#             dic[nums[i]] = i
#             if target == nums[i]:
#                 return [i, i]
#
#     def threeSum(self, nums, target):
#         dic = {}
#         for i in range(len(nums)):
#             next_target = target - nums[i]
#             indices = self.twoSum(nums[i + 1:], next_target)
#             if indices:
#                 return [i, i + 1 + indices[0], i + 1 + indices[1]]
#
#         return None





