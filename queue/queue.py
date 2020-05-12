"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList

# #Array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         # gets size of queue
#         return self.size

#     def enqueue(self, value):
#         # enqueue an item at the rear
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         # dequeue an item from front
#         if self.size > 0:

#             item_to_dequeue = self.storage[0]

#             self.storage = self.storage[1:]

#             self.size -= 1
#             return item_to_dequeue


# Linked List

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # gets size of queue
        return self.size

    def enqueue(self, value):
        # enqueue an item at the rear (back) of list (furthest to the left)
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # dequeue an item from front of list (furthest to the right)
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        return None
