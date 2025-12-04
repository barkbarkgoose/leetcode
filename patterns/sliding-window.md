# Sliding Window

Maintain a window of consecutive elements that expands or contracts based on conditions. Ideal for substring, subarray, or contiguous sequence problems with constraints.

**Key insight:** Instead of recalculating everything, slide the window by adding one element and removing another. Track window state (sum, characters, etc.) incrementally.

**Common problems:** Longest substring without repeating characters, minimum window substring, maximum sum subarray of size k, longest repeating character replacement.

**Example:** Finding longest substring with unique characters. Expand window by moving right pointer, contract by moving left pointer when duplicates appear.

```python
def longest_unique_substring(s):
    # Track the last seen index of each character
    char_map = {}
    
    # Sliding window: left and right pointers define the window boundaries
    # Window represents substring s[left:right+1] with all unique characters
    left = 0
    max_len = 0
    # Track the start and end indices of the longest substring found
    start = 0
    end = 0
    
    # Expand window by moving right pointer
    for right in range(len(s)):
        # If character already in window, contract from left
        # Move left pointer to position after last occurrence of duplicate
        if s[right] in char_map:
            # Use max() to ensure left only moves forward (never backward)
            left = max(left, char_map[s[right]] + 1)
            
        # Update last seen position of current character
        char_map[s[right]] = right
        
        # Update max length and substring indices: window size is (right - left + 1)
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            start = left
            end = right
    
    # Return the actual substring instead of just the length
    return s[start:end + 1]

# Example:
# Input: "abcabcbb"
# Output: "abc"
# Explanation: The longest substring without repeating characters is "abc" (length 3)
#
# Step-by-step with "abcabcbb":
# right=0, s[0]='a', char_map={}, left=0, window="a", max_len=1, result="a"
# right=1, s[1]='b', char_map={'a':0}, left=0, window="ab", max_len=2, result="ab"
# right=2, s[2]='c', char_map={'a':0,'b':1}, left=0, window="abc", max_len=3, result="abc"
# right=3, s[3]='a' (duplicate!), left=max(0,0+1)=1, window="bca", max_len=3, result="abc"
# right=4, s[4]='b' (duplicate!), left=max(1,1+1)=2, window="cab", max_len=3, result="abc"
# right=5, s[5]='c' (duplicate!), left=max(2,2+1)=3, window="abc", max_len=3, result="abc"
# right=6, s[6]='b' (duplicate!), left=max(3,4+1)=5, window="cb", max_len=3, result="abc"
# right=7, s[7]='b' (duplicate!), left=max(5,6+1)=7, window="b", max_len=3, result="abc"
```
