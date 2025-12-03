# Backtracking

Try possibilities recursively, undo (backtrack) when you hit invalid state. Essential for problems requiring exploring all combinations, permutations, or paths.

**Key insight:** Build solution incrementally. When you can't proceed further, undo last choice and try next option. Use recursion with state cleanup.

**Common problems:** Generate parentheses, subsets, permutations, combinations, N-queens, word search, sudoku solver, letter combinations of phone number.

**Example:** Generating all valid parentheses combinations. Add '(' or ')' at each step, backtrack when count of closing exceeds opening or when length limit reached.

```python
def generate_parentheses(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# Example usage:
result = generate_parentheses(3)
print(result)
# Expected output: ['((()))', '(()())', '(())()', '()(())', '()()()']
```

**Word Search Example:** Finding if a word exists in a 2D grid by exploring all paths. Mark cells as visited, try all directions, unmark when backtracking.

```python
def word_search(board, word):
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        if index == len(word):
            return True
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            board[row][col] != word[index]):
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Try all 4 directions
        found = (backtrack(row + 1, col, index + 1) or
                 backtrack(row - 1, col, index + 1) or
                 backtrack(row, col + 1, index + 1) or
                 backtrack(row, col - 1, index + 1))
        
        # Backtrack: unmark cell
        board[row][col] = temp
        return found
    
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False

# Example usage:
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(word_search(board, "ABCCED"))  # Expected output: True
print(word_search(board, "SEE"))     # Expected output: True
print(word_search(board, "ABCB"))    # Expected output: False
```
