"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21


Constraints:

    -2**31 <= x <= 2**31 - 1


"""
import time

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = ''
        if x < 0:
            sign = '-'
        
        reversedX = int(sign + str(abs(x))[::-1])

        # make sure we're in 32-bit integer range
        if not(-2**31 <= reversedX <= (2**31 - 1)):
            return 0
        
        return reversedX
    
    def reverse_optimized(self, x):
        """
        Fastest Python implementation that:
        1. Uses string operations which are highly optimized in Python
        2. Minimizes number of operations
        3. Uses a single range check
        """
        if x == 0:
            return 0
            
        # Convert to positive number and get sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Convert to string, reverse, and convert back
        result = int(str(x)[::-1])
        
        # Apply sign and check range
        result *= sign
        return result if -2**31 <= result <= 2**31 - 1 else 0


def time_function(func, x, iterations=100000):
    start = time.time()
    for _ in range(iterations):
        func(x)
    end = time.time()
    return (end - start) * 1000  # Convert to milliseconds


if __name__ == '__main__':
    test_cases = [
        123,
        -123,
        120,
        1563847412,
        0,
        2147483647,
        -2147483648
    ]
    
    print("Performance comparison (lower is better):")
    print("-" * 50)
    
    for x in test_cases:
        print(f"\nTesting with x = {x}")
        print(f"Original:    {time_function(Solution().reverse, x):.2f}ms")
        print(f"Optimized:     {time_function(Solution().reverse_optimized, x):.2f}ms")