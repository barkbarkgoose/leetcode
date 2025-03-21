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

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # create a list of encountered characters
        encountered_chars = []

        # iterate through string, keep track of longest substring thus far and starting index of current substring

        # any time a duplicate char is found, the starting index is reset to the next char after the first instance of the duplicate.

        # if the current substring is longer than the longest substring thus far, update the longest substring.

        # when end of string is reached OR the length of current substring PLUS the remaining characters is less than the longest substring, return the longest substring.

                