# Binary Search

Divide search space in half at each step by eliminating the half that cannot contain the answer. Works on sorted arrays or when you can determine which half to search.

**Key insight:** If you can determine whether answer is in left or right half, you can eliminate half the possibilities each iteration, achieving O(log n) time.

**Common problems:** Search in rotated sorted array, find peak element, search insert position, sqrt(x), first/last position of element, minimum in rotated array.

**Example:** Finding target in sorted array. Compare middle element to target, eliminate left half if target is greater, eliminate right half if target is smaller.

```python
def binary_search(nums, target):
    # Binary search: maintain left and right boundaries of search space
    # Start with entire array as search space
    left, right = 0, len(nums) - 1
    
    # Continue searching while search space is valid
    while left <= right:
        # Calculate midpoint: this is where we check the middle element
        mid = (left + right) // 2

        # Binary search pattern: compare middle element to target
        # If match found, return immediately
        if nums[mid] == target:
            return mid

        # If target is greater, eliminate left half (including mid)
        # Search space becomes [mid+1, right]
        elif nums[mid] < target:
            left = mid + 1

        # If target is smaller, eliminate right half (including mid)
        # Search space becomes [left, mid-1]
        else:
            right = mid - 1
    
    # Target not found in array
    return -1

# Example:
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
# Explanation: nums[4] = 9, which matches the target
#
# Step-by-step with [-1, 0, 3, 5, 9, 12], target = 9:
# left=0, right=5, mid=2: nums[2]=3 < 9, eliminate left half -> left=3
# left=3, right=5, mid=4: nums[4]=9 == 9, found! return 4
#
# Example with target = 2 (not found):
# left=0, right=5, mid=2: nums[2]=3 > 2, eliminate right half -> right=1
# left=0, right=1, mid=0: nums[0]=-1 < 2, eliminate left half -> left=1
# left=1, right=1, mid=1: nums[1]=0 < 2, eliminate left half -> left=2
# left=2, right=1: invalid (left > right), target not found -> return -1
```
