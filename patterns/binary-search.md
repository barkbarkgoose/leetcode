# Binary Search

Divide search space in half at each step by eliminating the half that cannot contain the answer. Works on sorted arrays or when you can determine which half to search.

**Key insight:** If you can determine whether answer is in left or right half, you can eliminate half the possibilities each iteration, achieving O(log n) time.

**Common problems:** Search in rotated sorted array, find peak element, search insert position, sqrt(x), first/last position of element, minimum in rotated array.

**Example:** Finding target in sorted array. Compare middle element to target, eliminate left half if target is greater, eliminate right half if target is smaller.

```python
def binary_search(nums, target):
    # start out by setting left and right indices to the start and end of our list
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # grab mid point of array
        mid = (left + right) // 2

        # always check if middle is what we want, return early if match
        if nums[mid] == target:
            return mid

        # eliminate left half if target is greater
        elif nums[mid] < target:
            left = mid + 1

        # eliminate right half if target is smaller
        else:
            right = mid - 1
    
    return -1
```
