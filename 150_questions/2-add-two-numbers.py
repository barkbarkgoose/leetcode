class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        returnNode = ListNode()
        currentNode = returnNode
        carry = 0

        # lists are in reverse order, can add from right to left like normal addition
        while l1 or l2 or carry > 0:
            # remainder (anything above 10 before the 10x multiplication) is to be carried to next position.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # if total is greater than 10, carry the remainder to next position
            carry = total // 10

            # set the current node's value to the remainder of total
            currentNode.val = total % 10
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # if there are still nodes to add, create a new node
            if l1 or l2 or carry > 0:
                currentNode.next = ListNode()
                currentNode = currentNode.next

        return returnNode

        
def createLinkedList(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


if __name__ == '__main__':
    solution = Solution()

    # output [7, 0, 8]
    n1 = ListNode(2, ListNode(4, ListNode(3)))  # 342
    n2 = ListNode(5, ListNode(6, ListNode(4)))  # 465
    result = solution.addTwoNumbers(n1, n2)

    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next

    print(result_list)

    l1 = [1,6,0,3,3,6,7,2,0,1]
    l2 = [6,3,0,8,9,6,6,9,6,1]

    n1 = createLinkedList(l1)
    n2 = createLinkedList(l2)

    result = solution.addTwoNumbers(n1, n2)

    result_list = []
    while result:
        result_list.append(result.val)
        result = result.next
    
    print(result_list)