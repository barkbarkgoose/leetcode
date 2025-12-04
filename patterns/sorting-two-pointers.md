# Sorting + Two Pointers

Sort the input first, then apply two pointers technique. Transforms O(n²) nested loop solutions into O(n log n) solutions for pair-finding problems.

**Key insight:** Sorting enables two pointers to work efficiently. After sorting, you can eliminate large portions of the search space by moving pointers based on comparisons.

**Common problems:** Three sum, four sum, closest sum, merge intervals, meeting rooms, array partition.

**Example:** Finding three numbers that sum to zero. Sort array, fix first number, then use two pointers on remaining array to find pairs that sum to negative of fixed number.

```python
def three_sum(nums):
    # Sort array to enable two-pointer technique
    nums.sort()
    result = []
    
    # Fix first number, then use two pointers for remaining two numbers
    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Two pointers: left starts after i, right starts at end
        # These pointers search for pairs that sum to -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicate values for left pointer
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                    
                left += 1

            elif current_sum < 0:
                # Sum too small, move left pointer right to increase sum
                left += 1

            else:
                # Sum too large, move right pointer left to decrease sum
                right -= 1
    
    return result

# Example:
# Input: [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation: Two triplets sum to zero: [-1, -1, 2] and [-1, 0, 1]
#
# Step-by-step with [-1, 0, 1, 2, -1, -4] (sorted: [-4, -1, -1, 0, 1, 2]):
# i=0, nums[i]=-4, left=1, right=5: sum = -4 + -1 + 2 = -3 < 0, left++
# i=0, nums[i]=-4, left=2, right=5: sum = -4 + -1 + 2 = -3 < 0, left++
# i=0, nums[i]=-4, left=3, right=5: sum = -4 + 0 + 2 = -2 < 0, left++
# i=0, nums[i]=-4, left=4, right=5: sum = -4 + 1 + 2 = -1 < 0, left++
# i=1, nums[i]=-1, left=2, right=5: sum = -1 + -1 + 2 = 0, found! result=[[-1,-1,2]]
# i=1, nums[i]=-1, left=3, right=5: sum = -1 + 0 + 2 = 1 > 0, right--
# i=1, nums[i]=-1, left=3, right=4: sum = -1 + 0 + 1 = 0, found! result=[[-1,-1,2],[-1,0,1]]
# i=2, nums[i]=-1 (duplicate, skip)
# i=3, nums[i]=0, left=4, right=5: sum = 0 + 1 + 2 = 3 > 0, right--
# (no more valid triplets)
```
