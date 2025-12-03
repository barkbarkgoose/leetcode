# Stack

Use LIFO (Last In, First Out) structure for matching, parsing, and tracking nested or hierarchical state. Perfect when you need to process elements in reverse order or match pairs.

**Key insight:** Push elements onto stack, pop when conditions are met. The last element added is the first one you need to process or match.

**Common problems:** Valid parentheses, daily temperatures, next greater element, evaluate reverse polish notation, decode string, largest rectangle in histogram.

**Example:** Checking if parentheses are valid. Push opening brackets, pop when matching closing bracket appears. Stack should be empty at end if valid.

```python
def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0
```
