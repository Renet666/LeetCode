# 141. Linked List Cycle

[LeetCode Problem 141](https://leetcode.com/problems/linked-list-cycle/)

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

A cycle exists if some node in the list can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle, otherwise `false`.

## Solutions

Two approaches are implemented, each in its own file. Both are correct and pass all test cases.

### 1. Floyd’s Tortoise and Hare (Optimal)

**File:** [`solution_floyd.py`](solution_floyd.py)

Uses two pointers moving at different speeds:
- `slow` moves one step at a time.
- `fast` moves two steps at a time.

If there is a cycle, the fast pointer will eventually lap the slow one (they meet). If the fast pointer reaches the end (`None`), there is no cycle.

#### Complexity
- **Time:** O(n) – linear in the number of nodes.
- **Space:** O(1) – only two pointers are used.

---

### 2. Hash Set (Simpler, but uses extra memory)

**File:** [`solution_hashset.py`](solution_hashset.py)

Traverses the list and stores each visited node in a set. If we ever encounter a node already in the set, a cycle exists.

#### Complexity
- **Time:** O(n) – linear.
- **Space:** O(n) – in the worst case we store all nodes (when no cycle).

LeetCode 9. Palindrome Number
Approach: Reverse Half of the Number (Mathematical)
- Time Complexity: O(log10(n))
- Space Complexity: O(1)
- Reverses only the second half of the integer and compares it to the first half.
