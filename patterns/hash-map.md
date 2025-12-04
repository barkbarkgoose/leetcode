# Hash Map Lookup

Use dictionaries or hash maps for O(1) lookups and tracking. Essential when you need to remember what you've seen, count frequencies, or map relationships.

**Key insight:** Trade space for time. Store information about elements as you process them, then query instantly instead of searching linearly.

**Common problems:** Two sum, group anagrams, first unique character, longest consecutive sequence, frequency counting, duplicate detection.

```python
def hash_map(nums):
    """
    Build a hash map from array values to their indices.
    Returns a dictionary mapping each value to its index.
    For duplicate values, stores the last occurrence's index.
    """
    map_dict = {}
    
    for i, num in enumerate(nums):
        map_dict[num] = i
    
    return map_dict
```

**Example:** Finding two numbers that sum to target. Store each number and its index as you iterate. For each new number, check if complement (target - number) exists in map.

```python
def two_sum(nums, target):
    """
    Find two numbers that sum to target using hash map lookup.
    Uses hash_map() to build lookup structure, then checks for complement pairs.
    """
    num_map = hash_map(nums)

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map and num_map[complement] != i:
            return [num_map[complement], i]

    return []
```

**Example:** Longest consecutive sequence. Use a hash map to store all numbers for O(1) lookup. For each number, check if it's the start of a sequence (no number-1 exists), then expand rightward to count consecutive numbers.

```python
def longest_consecutive(nums):
    """
    Find longest consecutive sequence using hash map for O(1) lookups.
    Uses hash_map() to create lookup structure, then finds sequence starts and expands.
    """
    # Hash map: Store all numbers for O(1) lookup
    # This allows us to quickly check if a number exists in the array
    # Note: Using hash_map keys automatically handles duplicates, which is perfect here
    # since duplicates don't affect consecutive sequences (e.g., [1,2,2,3] -> sequence [1,2,3])
    num_map = hash_map(nums)
    max_length = 0

    for num in num_map:
        # Hash map application: Check if current number is start of sequence
        # Only process if (num - 1) doesn't exist, meaning this is the beginning
        if (num - 1) not in num_map:
            current_num = num
            current_length = 1

            # Hash map application: Expand sequence by checking if next number exists
            # Use O(1) lookup to find consecutive numbers instead of O(n) search
            while (current_num + 1) in num_map:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length
```
