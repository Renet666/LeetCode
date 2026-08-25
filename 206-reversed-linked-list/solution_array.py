from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    # Reverse the links by iterating backwards
    for i in range(len(nodes) - 1, 0, -1):
        nodes[i].next = nodes[i - 1]

    nodes[0].next = None  # new tail
    return nodes[-1]  # new head
