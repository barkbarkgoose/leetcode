"""
Given a string s, find the length of the longest

without duplicate characters.

Example 1:

  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.

Example 2:

  Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.

Example 3:

  Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.
  Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

Optimization Suggestions:
1. Use a dictionary/hash map instead of a list to store character positions - this changes 
   the lookup time from O(n) to O(1)
2. Use a sliding window with two pointers instead of list slicing - this avoids creating 
   new lists on each duplicate character
3. The early break condition could be simplified since we already know the maximum possible 
   length from the remaining string
4. Could use set() instead of list() for encountered_chars if we only need to track existence 
   (but wouldn't work with current sliding window approach)

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s) -> int:
        """
        :type s: str
        :rtype: int
        """
        encountered_chars = []
        longest_substring = 0
        
        for index, char in enumerate(s):
            if (len(encountered_chars) + len(s) - (index + 1)) < longest_substring:
                break

            # if char is already in list, remove everything from that position toward front of list
            if char in encountered_chars:
                char_index = encountered_chars.index(char)
                encountered_chars = encountered_chars[char_index + 1:]
            
            # always add char to list
            encountered_chars.append(char)
            
            if longest_substring < len(encountered_chars):
                longest_substring = len(encountered_chars)
                
        return longest_substring
    
    def optimizedSolution(self, s) -> int:
        """
        Optimized version using sliding window and dictionary
        :type s: str
        :rtype: int
        """
        # Optimization 1: Using dictionary instead of list for O(1) lookups
        # This replaces the O(n) operation of list.index()
        char_position = {}
        longest_substring = 0
        
        # Optimization 2: Sliding window implementation
        # 'start' and 'end' are the window pointers, avoiding list slicing operations
        start = 0
        
        for end, char in enumerate(s):
            # Optimization 2 continued: Window management
            # Instead of creating new lists with slicing, we just move the 'start' pointer
            if char in char_position and char_position[char] >= start:
                start = char_position[char] + 1
            else:
                # Optimization 3: Direct length calculation
                # Instead of maintaining a list and checking its length,
                # we calculate window size directly with (end - start + 1)
                longest_substring = max(longest_substring, end - start + 1)
            
            # Optimization 1 continued: O(1) position updates
            # Simply update dictionary instead of list operations
            char_position[char] = end
                
        return longest_substring


if __name__ == '__main__':
    solution = Solution()
    
    # Test cases from the examples
    test_cases = [
        "abcabcbb",  # should return 3
        "bbbbb",     # should return 1
        "pwwkew",    # should return 3
        "",         # edge case, should return 0
    ]
    
    print("Original solution:")
    for test in test_cases:
        result = solution.lengthOfLongestSubstring(test)
        print(f'Input: "{test}"')
        print(f'Output: {result}\n')

    print("Optimized solution:")
    for test in test_cases:
        result = solution.optimizedSolution(test)
        print(f'Input: "{test}"')
        print(f'Output: {result}\n')
                