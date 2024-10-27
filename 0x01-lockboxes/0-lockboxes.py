#!/usr/bin/python3
"""Lockboxes challenge script"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""

    n = len(boxes)
    opened_boxes = [False] * n
    opened_boxes[0] = True
    current_stack = [0]

    while current_stack:
        current_box = current_stack.pop()
        for key in boxes[current_box]:
            if key < n and not opened_boxes[key]:
                opened_boxes[key] = True
                current_stack.append(key)

    return all(opened_boxes)
