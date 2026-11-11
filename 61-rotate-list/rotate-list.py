
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the linked list
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Reduce unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Step 3: Connect tail to head (make circular list)
        tail.next = head

        # Step 4: Find the new tail
        steps = length - k
        new_tail = head

        for i in range(steps - 1):
            new_tail = new_tail.next

        # Step 5: Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
