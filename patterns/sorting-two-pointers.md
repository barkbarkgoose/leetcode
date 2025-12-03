# Sorting + Two Pointers

Sort the input first, then apply two pointers technique. Transforms O(n²) nested loop solutions into O(n log n) solutions for pair-finding problems.

**Key insight:** Sorting enables two pointers to work efficiently. After sorting, you can eliminate large portions of the search space by moving pointers based on comparisons.

**Common problems:** Three sum, four sum, closest sum, merge intervals, meeting rooms, array partition.

**Example:** Finding three numbers that sum to zero. Sort array, fix first number, then use two pointers on remaining array to find pairs that sum to negative of fixed number.

```python
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result
```
