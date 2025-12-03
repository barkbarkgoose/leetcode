# Prefix Sum

Precompute cumulative sums (or other cumulative operations) to answer range queries instantly. Eliminates need to recalculate sums for overlapping ranges.

**Key insight:** Build prefix array where each index contains sum of all previous elements. Range sum from i to j equals prefix[j] - prefix[i-1].

**Common problems:** Subarray sum equals k, range sum queries, maximum subarray, product of array except self, continuous subarray sum.

**Example:** Finding number of subarrays with sum k. Build prefix sums, then for each prefix sum, check if (prefix_sum - k) exists in previous prefix sums.

```python
def subarray_sum_equals_k(nums, k):
    prefix_sum = {0: 1}
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    
    return count
```
