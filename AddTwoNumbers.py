# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        return l3

    def addTwoNumbersBad(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        l3_prev = l3
        l3_cur = l3

        while True:
            if l1 == None and l2 != None:
                sum_val = 0 + l2.val + l3_cur.val
                if sum_val >= 10:
                    l3_cur.val = sum_val % 10
                    l3_cur.next = ListNode(sum_val // 10)
                else:
                    l3_cur.val = sum_val
                    l3_cur.next = ListNode(0)
                l2 = l2.next
                l3_prev = l3_cur
                l3_cur = l3_cur.next
            elif l1 != None and l2 == None:
                sum_val = l1.val + 0 + l3_cur.val
                if sum_val >= 10:
                    l3_cur.val = sum_val % 10
                    l3_cur.next = ListNode(sum_val // 10)
                else:
                    l3_cur.val = sum_val
                    l3_cur.next = ListNode(0)
                l1 = l1.next
                l3_prev = l3_cur
                l3_cur = l3_cur.next
            elif l1 == None and l2 == None:
                if l3_cur.val == 0:
                    l3_prev.next = None
                return l3
            else:
                sum_val = l1.val + l2.val + l3_cur.val
                    
                if sum_val >= 10:
                    l3_cur.val = sum_val % 10
                    l3_cur.next = ListNode(sum_val // 10)
                else:
                    l3_cur.val = sum_val
                    l3_cur.next = ListNode(0)
                l1 = l1.next
                l2 = l2.next
                l3_prev = l3_cur
                l3_cur = l3_cur.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(2)

    l2 = ListNode(1)
    l2.next = ListNode(8)
    l2.next.next = ListNode(0)
    l2.next.next.next = ListNode(4)

    solution = Solution()
    l3 = solution.addTwoNumbers(l1, l2)
    print(l3.val, l3.next.val, l3.next.next.val, l3.next.next.next.val)