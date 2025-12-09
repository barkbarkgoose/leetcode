"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

-----

Example 1:

Input: num = 3749
Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

-----

Example 2:

Input: num = 58
Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
"""

import math

int_map = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

# --- helper classes ---
def get_subtractive_num(x, power):
    pre_symbol = int_map[1*power]
    post_symbol = int_map[(x+1)*power]

    return f'{pre_symbol}{post_symbol}'

def get_normal_num(x, power):
    symbol = ''
    new_x = x

    # account for the "half" values (5, 50, 500)
    if x >= 5:
        symbol = int_map[5*power]
        new_x -= 5

    remainder_symbol = int_map[1*power]

    return symbol + remainder_symbol * new_x



class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = str(num)
        power = int(10**(len(num_str) - 1))
        digits_list = [int(x) for x in num_str]

        result = ''

        for x in digits_list:
            if x in (4, 9):
                result += get_subtractive_num(x, power)

            else:
                result += get_normal_num(x, power)
            
            power = int(max((power/10), 1))

        return result


# --- Optimized Solution ---

# Pre-computed mapping of all Roman numeral values in descending order
# Includes subtractive cases (900, 400, 90, 40, 9, 4) for efficient lookup
ROMAN_VALUES = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def optimized_solution(num: int) -> str:
    """
    Convert an integer to a Roman numeral using a greedy algorithm.
    
    This optimized approach:
    - Uses a pre-computed list of value-symbol pairs (including subtractive cases)
    - Employs a greedy strategy: always subtract the largest possible value
    - Builds the result using a list (O(1) append) instead of string concatenation
    - Avoids string conversions and repeated power calculations
    
    Time Complexity: O(1) - The number of iterations is bounded by the number of Roman numeral symbols (13), regardless of input size
    
	Space Complexity: O(1) - The result list size is bounded by the maximum Roman numeral length (which is constant)
    
    Args:
        num: Integer to convert (1 <= num <= 3999)
        
    Returns:
        String representation of the Roman numeral
        
    Example:
        >>> optimized_solution(3749)
        'MMMDCCXLIX'
        >>> optimized_solution(1994)
        'MCMXCIV'
    """
    # Use a list to build the result (more efficient than string concatenation)
    result_parts = []
    
    # Greedy approach: repeatedly subtract the largest possible value
    for value, symbol in ROMAN_VALUES:
        # Count how many times this value fits into the remaining number
        count = num // value
        
        # Append the symbol that many times
        if count > 0:
            result_parts.append(symbol * count)
            num -= value * count
        
        # Early exit if we've processed the entire number
        if num == 0:
            break
    
    # Join all parts into a single string
    return ''.join(result_parts)