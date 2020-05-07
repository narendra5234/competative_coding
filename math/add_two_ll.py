class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def add_two(l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        curr = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, output = divmod(val1 + val2 + carry, 10)

            curr.next = ListNode(output)
            curr = curr.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next