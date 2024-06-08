class Solution:
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum_val = digit1 + digit2 + carry
            digit = sum_val % 10
            carry = sum_val // 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next
