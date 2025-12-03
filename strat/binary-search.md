# Binary Search

Divide search space in half at each step by eliminating the half that cannot contain the answer. Works on sorted arrays or when you can determine which half to search.

**Key insight:** If you can determine whether answer is in left or right half, you can eliminate half the possibilities each iteration, achieving O(log n) time.

**Common problems:** Search in rotated sorted array, find peak element, search insert position, sqrt(x), first/last position of element, minimum in rotated array.

**Example:** Finding target in sorted array. Compare middle element to target, eliminate left half if target is greater, eliminate right half if target is smaller.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```
