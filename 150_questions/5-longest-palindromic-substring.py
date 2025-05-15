class Solution:
    """
    Given a string s, return the longest palindromic substring in s.

    will use two pointers to find the longest palindrome

    create a sliding window that starts with the entire string, decreases in length and shifts one position "scanning" over the string with each subsequent downsize.

    the first palindrome found will be the longest

    example:
        input: "babad"
        output: "bab"
        explanation: "aba" is also a valid answer

    example 2:
        input: "cbbd"
        output: "bb"
    """
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        # If the string is empty or has only one character, return the string itself
        if len(s) == 1:
            return s

        # Initialize variables to store the longest palindrome
        end_index = (len(s) - 1)
        left, right = 0, end_index
        window_length = end_index + 1

        # the smallest possible length is 2
        while window_length > 0:
            while right <= end_index:
                window = s[left:(right + 1)]

                if window == window[::-1]:
                    return window

                else:
                    left += 1
                    right += 1

            # shrink window by 1 and reset scan position
            window_length -= 1
            left, right = 0, (window_length - 1)

    def optimizedLongestPalindrome(self, s: str) -> str:
        """
        Optimized version using center expansion approach

        iterates over whole string and trys expanding "window" on each letter to check if it, plus its neighbors are a palindrome.

        :type s: str
        :rtype: str
        """
        # Optimization: Early return for edge cases
        if not s or len(s) < 2:
            return s

        start = 0
        max_length = 1

        def expand_around_center(left: int, right: int) -> tuple:
            """
            helper function to get indices for window in center of string    

            :type left: int - left indices
            :type right: int - right indices
            :rtype: tuple - left and right indices
            """
            # keep expanding window so long as ends are same (is palindrome thus far)
            while True:
                ends_in_bounds = left >= 0 and right < len(s)
                
                if not ends_in_bounds or not (s[left] == s[right]):
                    break;
                
                left -= 1
                right += 1

            return left + 1, right - 1

        # Optimization: Center expansion approach
        # Instead of checking all possible substrings, we expand from each possible center
        # if difference (length) between returned indices is greater than current max length, update start and max_length
        print("I got here")
        for i in range(len(s)):
            # Check for odd length palindromes
            left, right = expand_around_center(i, i)
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1

            # Check for even length palindromes
            left, right = expand_around_center(i, i + 1)
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1

        # Optimization: Single string slice at the end
        # Instead of creating multiple substrings during the process
        return s[start:start + max_length]


if __name__ == "__main__":
    s = "babad"
    print("Original solution:")
    print(Solution().longestPalindrome(s))
    print("\nOptimized solution:")
    print(Solution().optimizedLongestPalindrome(s))

    s = "cbbd"
    print("\nOriginal solution:")
    print(Solution().longestPalindrome(s))
    print("\nOptimized solution:")
    print(Solution().optimizedLongestPalindrome(s))