"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

__Example 1:__

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

__Example 2:__

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

__Example 3:__

    Input: s = "A", numRows = 1
    Output: "A"

__Constraints:__

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
"""

class Solution:
    """
    given number of rows, create a dictionary with each row as the key and the output as the value: e.g.: { 1: 'P A H N' }
        - when we go to print the value each row can be printed completely without any further lookups or loops.
    
    Total number of columns is determined with:
        - string length (lenString) 
        - rows (numRows)
    
    **a solid column is a column that fills the full length of numRows**
    **inner columns are the "zag", the diagonal rows with a single letter in each column**
    """
    def convert(self, s: str, numRows: int) -> str:
        isSolidColumn = True
        row = 0
        zigDict = {i: '' for i in range(numRows)}

        # handle edge cases where numrows is 0 or 1
        if numRows == 0:
            return

        if numRows == 1:
            return s
        
        for character in s:
            zigDict[row] += character
            
            # when numRows is 2, ignore the value for isSolidColumn
            if isSolidColumn or numRows == 2:
                # vertical column. if reaches the bottom row, reverse direction and switch to diagonal
                if row == (numRows - 1):
                    isSolidColumn = False
                    row -= 1
                    
                else:
                    row += 1
            
            # diagonal row
            else:
                if row == 1:
                    isSolidColumn = True
                
                if row != 0:
                    row -= 1
                
        outputString = ''
        for outputRow in zigDict:
            outputString += zigDict[outputRow]
            
        return outputString
        
        
if __name__ == '__main__':
    # expected: "PAHNAPLSIIGYIR"
    Solution().convert('PAYPALISHIRING', 3)
    
    # expected: "ACBD"
    Solution().convert('ABCD', 2)