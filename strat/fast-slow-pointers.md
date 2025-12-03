# Fast/Slow Pointers

Use two pointers moving at different speeds through a linked list or array. Essential for detecting cycles, finding middle elements, or solving problems with linked list constraints.

**Key insight:** Fast pointer moves two steps while slow moves one. They'll meet if there's a cycle, or fast will reach end while slow is at middle.

**Common problems:** Linked list cycle detection, find middle of linked list, palindrome linked list, remove nth node from end, cycle start detection.

**Example:** Detecting cycle in linked list. If fast and slow pointers meet, cycle exists. If fast reaches null, no cycle.

```python
def has_cycle(head):
    if not head:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
```
