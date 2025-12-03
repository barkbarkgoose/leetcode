# Hash Map Lookup

Use dictionaries or hash maps for O(1) lookups and tracking. Essential when you need to remember what you've seen, count frequencies, or map relationships.

**Key insight:** Trade space for time. Store information about elements as you process them, then query instantly instead of searching linearly.

**Common problems:** Two sum, group anagrams, first unique character, longest consecutive sequence, frequency counting, duplicate detection.

**Example:** Finding two numbers that sum to target. Store each number and its index as you iterate. For each new number, check if complement (target - number) exists in map.

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```
