"""
Given an integer x, return true if x is a

, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

    -231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""
import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # a negative number is never a palindrome
        if x < 0:
            return False

        # quick and dirty...
        return str(x) == str(x)[::-1]
    
    def isPalindromeNonString(self, x):
        """
        determine if number is a palindrome, without converting it to a string first

        :type x: int
        :rtype: bool
        """
        # a negative number is never a palindrome
        if x < 0:
            return False
            
        # if number ends with 0, it can't be a palindrome
        # (except for 0 itself)
        if x != 0 and x % 10 == 0:
            return False
            
        # reverse the second half of the number
        reversed_num = 0
        while x > reversed_num:
            # x % 10 will always grab the last digit (it's the only one not divisible by 10)
            reversed_num = reversed_num * 10 + x % 10
            # remove last digit from number
            x //= 10
            
        # when the original number is less than or equal to reversed_num,
        # we've processed half or more of the digits
        # for even length numbers: x == reversed_num
        # for odd length numbers: x == reversed_num // 10
        return x == reversed_num or x == reversed_num // 10


if __name__ == '__main__':
    print('--- string conversion method ---')
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))

    print('\n--- non string method ---')
    print(Solution().isPalindromeNonString(121))
    print(Solution().isPalindromeNonString(-121))
    print(Solution().isPalindromeNonString(10))
