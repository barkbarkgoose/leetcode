"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
class Solution:
    def __init__(self):
        self.s = ''
        self.p = ''
        self.run_sanity_check = False

    def sanity_check(self):
        """
        sanity check to test out things as I go
        """
        if not self.run_sanity_check:
            return

        section = '\n--- accessing final value in a string ---'
        print(section)
        my_list = ['a', 'b']
        print(my_list[-1])



    def solution(self) -> bool:
        section = '\n--- SOLUTION ---'
        print(section)

        # get reversed copy of p, break up into tokens
        p_reversed = self.p[::-1]
        tokens = ['']
        star_found = False
        for e in p_reversed:
            if star_found:
                tokens[-1] += e
                star_found = False
                continue

            else:
                pass

    def isMatch(self, s: str, p: str) -> bool:
        """
        --- example case 1 ---
            s1 = aaxcab
            p1 = a*aab*.*b (should match)

        --- example case 2 ---
            s2 = aaxcabz
            p2 = a*aab*.*b (no match because of final "z")
        """
        self.s = s
        self.p = p

        self.sanity_check()

        return self.solution()

if __name__ == '__main__':
    solution = Solution()
    solution.run_sanity_check = True
    solution.isMatch('aaxcab', 'a*aab*.*b')