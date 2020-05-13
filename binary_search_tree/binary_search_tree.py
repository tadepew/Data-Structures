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


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            # if empty
            self.value.insert(value)
            return value

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
        if not self.value:
            return False

        if self.right:
            return self.right.get_max()

        else:
            return self.value

        # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if self.value:
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)
        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
