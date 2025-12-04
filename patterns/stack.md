# Stack

Use LIFO (Last In, First Out) structure for matching, parsing, and tracking nested or hierarchical state. Perfect when you need to process elements in reverse order or match pairs.

**Key insight:** Push elements onto stack, pop when conditions are met. The last element added is the first one you need to process or match.

**Common problems:** Valid parentheses, daily temperatures, next greater element, evaluate reverse polish notation, decode string, largest rectangle in histogram.

**Example:** Checking if parentheses are valid. Push opening brackets, pop when matching closing bracket appears. Stack should be empty at end if valid.

```python
def is_valid_parentheses(s):
    # Stack stores opening brackets in LIFO order
    # When closing bracket appears, it should match the most recent opening bracket
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # If closing bracket, check if it matches the most recent opening bracket
        if char in pairs:
            # Stack empty or no matching opening bracket = invalid
            if not stack or stack.pop() != pairs[char]:
                return False
                
        else:
            # Push opening brackets onto stack
            stack.append(char)
    
    # Valid if all brackets were matched (stack is empty)
    return len(stack) == 0

# Example:
# Input: "()[]{}"
# Output: True
# Explanation: All brackets are properly matched and nested
#
# Step-by-step with "()[]{}":
# char='(', stack=[], push '(' -> stack=['(']
# char=')', stack=['('], pop '(' matches ')' -> stack=[]
# char='[', stack=[], push '[' -> stack=['[']
# char=']', stack=['['], pop '[' matches ']' -> stack=[]
# char='{', stack=[], push '{' -> stack=['{']
# char='}', stack=['{'], pop '{' matches '}' -> stack=[]
# Final: stack is empty -> return True
#
# Example with invalid: "([)]"
# char='(', stack=[], push '(' -> stack=['(']
# char='[', stack=['('], push '[' -> stack=['(', '[']
# char=')', stack=['(', '['], pop '[' != '(', mismatch! -> return False
```
