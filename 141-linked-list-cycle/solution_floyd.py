from typing import Optional
from listnode import ListNode


def hasCycle(self, head: Optional[ListNode]) -> bool:
    """Floyd's Tortoise and Hare algorithm."""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
