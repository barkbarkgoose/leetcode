# Two Pointers

Use two pointers that move through an array or string, either toward each other or in the same direction. Perfect for problems where you need to find pairs, check palindromes, or process elements in relation to each other.

**Key insight:** Instead of nested loops, use two pointers to eliminate possibilities in a single pass. One pointer typically starts at the beginning, the other at the end, or both start together and move at different speeds.

**Common problems:** Two sum in sorted array, palindrome checking, removing duplicates, container with most water, three sum.

**Example:** Finding two numbers that sum to a target in a sorted array. Start pointers at both ends, move left pointer right if sum is too small, move right pointer left if sum is too large.

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```
