# nums = [11, 15, 2, 7]
# i, j = 0, 1
# # print()

# # for i in nums:
# #     for j in nums:
# #         print(i,j)



# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     # """
#     # seen = {}
#     # i = 0

#     # while i < len(nums):
#     #     if nums[i] not in seen:

#     #         seen[nums[i]] = i
#     #         print(f"added {i} to {seen} ")
#     #         # seen = {"11": "0",  }
#     #     compliment = abs(nums[i] - target)
#     #     print("Compliment: ", compliment)
#     #     if compliment in seen:
#     #         return seen[compliment], i
#     #     else:
#     #         i += 1


#     for i in nums:
#         for j in nums:
#             print(i,j)

# print(twoSum(nums, 9))

class Solution(object):
    def twoSum(self, nums, target):
    
        :type nums: List[2, 7, 11, 15]
        :type target: 9
        :rtype: List(0,1)