# Two Pointers

Use two pointers that move through an array or string, either toward each other or in the same direction. Perfect for problems where you need to find pairs, check palindromes, or process elements in relation to each other.

**Key insight:** Instead of nested loops, use two pointers to eliminate possibilities in a single pass. One pointer typically starts at the beginning, the other at the end, or both start together and move at different speeds.

**Common problems:** Two sum in sorted array, palindrome checking, removing duplicates, container with most water, three sum.

**Example:** Finding two numbers that sum to a target in a sorted array. Start pointers at both ends, move left pointer right if sum is too small, move right pointer left if sum is too large.

```python
def two_sum_sorted(nums, target):
    # Two pointers: left starts at beginning, right starts at end
    # Since array is sorted, we can eliminate possibilities by moving pointers
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            # Found the pair
            return [left, right]
            
        elif current_sum < target:
            # Sum too small, move left pointer right to increase sum
            left += 1

        else:
            # Sum too large, move right pointer left to decrease sum
            right -= 1
    
    return []

# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9
#
# Step-by-step with [2, 7, 11, 15], target = 9:
# left=0, right=3: sum = 2 + 15 = 17 > 9, right--
# left=0, right=2: sum = 2 + 11 = 13 > 9, right--
# left=0, right=1: sum = 2 + 7 = 9 == 9, found! return [0, 1]
#
# Example with target = 18:
# left=0, right=3: sum = 2 + 15 = 17 < 18, left++
# left=1, right=3: sum = 7 + 15 = 22 > 18, right--
# left=1, right=2: sum = 7 + 11 = 18 == 18, found! return [1, 2]
```
