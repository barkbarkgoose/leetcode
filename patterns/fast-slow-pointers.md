# Fast/Slow Pointers

Use two pointers moving at different speeds through a linked list or array. Essential for detecting cycles, finding middle elements, or solving problems with linked list constraints.

**Key insight:** Fast pointer moves two steps while slow moves one. Within a cycle, fast gains 1 step per iteration on slow, so it will eventually catch up. If no cycle, fast reaches null first.

**Common problems:** Linked list cycle detection, find middle of linked list, palindrome linked list, remove nth node from end, cycle start detection.

**Example:** Detecting cycle in linked list. A cycle means any node points back to a previous node (not necessarily last→first). If fast and slow pointers meet, cycle exists. If fast reaches null, no cycle.

```python
def has_cycle(head):
    # Cycle means any node points back to a previous node
    # Examples: A->B->C->D->B (D points back to B), or A->B->C->A (circular)
    if not head:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

# Example trace for 1->2->3->4->1 (circular):
# Start: slow=1, fast=1
# Iter 1: slow=2, fast=3 (2 != 3, continue)
# Iter 2: slow=3, fast=1 (3 != 1, continue) 
# Iter 3: slow=4, fast=3 (4 != 3, continue)
# Iter 4: slow=1, fast=1 (1 == 1, cycle detected!)
# 
# Fast pointer "catches up" because it moves 2x speed within the cycle
# 
# Other examples:
# 1->2->3->4->2 (node 4 points back to node 2) = cycle exists
# 1->2->3->4->None = no cycle
```
