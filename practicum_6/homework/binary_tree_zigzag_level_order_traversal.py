from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self) -> list[Any]:
        if not self.root:
            return []
        result = []
        level = 0
        queue = [self.root]

        while queue:
            level_size = len(queue)
            level_list = []

            for i in range(level_size):
                node = queue.pop(0)
                level_list.append(node.key)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                level_list.reverse()

            result.append(level_list)
            level += 1
        return result


def build_tree(list_view: list[Any]) -> BinaryTree:
    bt = BinaryTree()

    if not list_view:
        return bt
    queue = []
    bt.root = Node(list_view[0])
    queue.append(bt.root)
    i = 1

    while queue:
        node = queue.pop(0)

        if i < len(list_view):
            if list_view[i] is not None:
                node.left = Node(list_view[i])
                queue.append(node.left)
            i += 1

        if i < len(list_view):
            if list_view[i] is not None:
                node.right = Node(list_view[i])
                queue.append(node.right)
            i += 1
    return bt


if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "practicum_6/homework/binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
