"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if self.value > value:
            # if tree node is greater than value to insert, go left
            if self.left:
                # works recursively and returns true
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

        else:
            # if tree node is less than or equal to value to insert, go right
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # when we start searching self will be the root
        # with recursion we always need to define our criteria for stopping
        if target == self.value:
            return True  # cascades back up

        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)

        if target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)

        # else:
        #     return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()

        else:
            return self.value

        # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        to_visit = [node]
        while to_visit:
            current = to_visit.pop(0)
            print(current.value)
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()

        stack.push(node)

        while stack:
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(node)
        if self.right:
            self.right.post_order_dft(node)
        print(self.value)

# Draw out test BST
#      1
#        \
#         8
#         /
#        5
#      /   \
#    3      7
#   / \    /
#  2   4  6
#
# post order traversal explanation
# post order traverses farthest left, then right, then root node
# at 1, if left go left, there is no left so we go right
# at 8, if left go left, there is left so we go go 5
# at 5, left exists so go to 3
# at 3, left exists so go to 2
# at 2, no left and no right so print value 2
# [2, ]
# left of 3 if statement is done, so go right of 3
# at 3, right exists go to 4
# at 4, no left and no right so print value 4
# [2, 4, ]
# all left and all right of 3 are taken care of, so go to 5
# all left of 5 is done, so go right to 7
# at 7, left exists go to 6
# at 6, no left and no right so print value 6
# [2, 4, 6, ]
# back up to 7, all left is done, so go right, no right so print 7
# [2, 4, 6, 7, ]
# back up to 5, all left and all right is done, so print 5
# [2, 4, 6, 7, 5, ]
# back up to 8, left is gone so go right, no right exists so print 8
# [2, 4, 6, 7, 5, 8, ]
# back up to 1, right is taken care of so print 1
# [2, 4, 6, 7, 5, 8, 1]
# finished recursive traversion
