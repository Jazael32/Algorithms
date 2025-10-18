class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergeTwoLists(self, l1: ListNode, l2:ListNode) -> ListNode:
        mergedList = tmp = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        tmp.next = l1 or l2
        return mergedList.next

    def print_list(self, node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

sol = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

result = sol.mergeTwoLists(l1, l2)
sol.print_list(result)