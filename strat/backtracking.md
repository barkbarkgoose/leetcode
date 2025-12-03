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
```
