# Prefix Sum

Precompute cumulative sums (or other cumulative operations) to answer range queries instantly. Eliminates need to recalculate sums for overlapping ranges.

**Key insight:** Build prefix array where each index contains sum of all previous elements. Range sum from i to j equals prefix[j] - prefix[i-1].

**Common problems:** Subarray sum equals k, range sum queries, maximum subarray, product of array except self, continuous subarray sum.

**Example:** Finding number of subarrays with sum k. Build prefix sums, then for each prefix sum, check if (prefix_sum - k) exists in previous prefix sums.

```python
def prefix_sum(nums):
    """
    Build prefix sum array where prefix[i] = sum of nums[0] to nums[i-1].
    Returns a list where prefix[i] contains the cumulative sum up to index i-1.
    """
    prefix = [0]
    current_sum = 0
    
    for num in nums:
        current_sum += num
        prefix.append(current_sum)
    
    return prefix


def subarray_sum_equals_k(nums, k):
    """
    Find number of subarrays with sum k using prefix sum technique.
    Uses prefix_sum() to build cumulative sums, then tracks frequencies in a map.
    For each cumulative sum, check if (current_sum - k) exists in previous sums.
    """
    prefix = prefix_sum(nums)
    prefix_map = {0: 1}
    count = 0
    
    # Skip prefix[0] which is always 0, process actual cumulative sums
    for i in range(1, len(prefix)):
        current_sum = prefix[i]
        
        if current_sum - k in prefix_map:
            count += prefix_map[current_sum - k]
        
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
    
    return count
```
