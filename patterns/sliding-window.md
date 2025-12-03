# Sliding Window

Maintain a window of consecutive elements that expands or contracts based on conditions. Ideal for substring, subarray, or contiguous sequence problems with constraints.

**Key insight:** Instead of recalculating everything, slide the window by adding one element and removing another. Track window state (sum, characters, etc.) incrementally.

**Common problems:** Longest substring without repeating characters, minimum window substring, maximum sum subarray of size k, longest repeating character replacement.

**Example:** Finding longest substring with unique characters. Expand window by moving right pointer, contract by moving left pointer when duplicates appear.

```python
def longest_unique_substring(s):
    char_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len
```
