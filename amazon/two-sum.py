"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

-----

notes:
- nums: List[int]
- target: int

output -> List[int]

#### process
go through list, find first numer that is a factor of target
    - a % b -> True/False

keep going, multipy first factor by each number and see if result is target.

if no match between factor and other number to target, move on to get different factor

"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for number in nums:
            next_index = nums.index(number) + 1

            while next_index < len(nums):
                if number + nums[next_index] == target:
                    return [nums.index(number), next_index]

                next_index += 1


# --------------------------------- main ---------------------------------
if __name__ == '__main__':
    SolutionA = Solution()

    # output -> [0,1]
    result = SolutionA.twoSum([2, 7, 11, 15], 9)
    print(result)

    print('\n------------------------\n')

    # output -> [1, 2]
    result = SolutionA.twoSum([3, 2, 4], 6)
    print(result)

    print('\n------------------------\n')

    # output -> [0, 4]
    result = SolutionA.twoSum([0, 3, -3, 4, -1], -1)
    print(result)

