class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self):
        self.head = None

    def add_to_tail(self, value):

        new_node = Node(value)
        # what if the list is empty?
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            current = self.head

            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list
            current.set_next(new_node)

    def remove_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            head_value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return head_value
