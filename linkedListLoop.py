# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def __init__(self):
        linked_list = ListNode(10)
        linked_list.next = ListNode(15)
        linked_list.next.next = ListNode(17)
        linked_list.next.next.next = ListNode(19)
        linked_list.next.next.next.next = linked_list.next
        if self.detect_cycle(linked_list) is not None:
            print self.detect_cycle(linked_list).val
        else:
            print ("None")

    def detect_cycle(self, a):
        if a is None:
            return a
        if a.next is None:
            return a
        p1 = a
        p2 = a
        b = 0


        while p1 is not None and p2 is not None:

            p1 = p1.next

            if p2.next is not None:
                p2 = p2.next.next
            else:
                p2 = None
            if p1 == p2 and p1 is not None and p2 is not None:
                return p1
        return None


if __name__ == '__main__':
    solution = Solution()
