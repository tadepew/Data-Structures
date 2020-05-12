"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
            self.length += 1

        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

  # we already have access to the head so no need to traverse

    def remove_from_head(self):

        if not self.head:
            return None

        else:
            if self.head != self.tail:
                head_to_remove = self.head
                self.head = head_to_remove.next
                # new head is the old head's next node
                self.length -= 1
                return head_to_remove

            else:
                removed_head = self.head.value
                self.head = self.tail = None
                self.length -= 1
                return removed_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    # add value to end
    # set as tail
    # set old tail as new tail's previous node

# we have access to the end of the list, so we can directly add new nodes O(1)
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
            self.length += 1

        else:
            # set current tail's next to the new node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if not self.tail:
            return None

        else:
            if self.tail != self.head:
                # if more than one value
                tail_to_remove = self.tail
                self.tail = tail_to_remove.prev
                # new tail is the old tail's previous node
                self.length -= 1
                return tail_to_remove

            else:
                removed_tail = self.tail.value
                self.tail = self.head = None
                self.length -= 1
                return removed_tail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):

        if not self.head and not self.tail:
            return None

        else:

            current = self.head

            while current is not None:
                current = current.next
                if current == node:
                    # prev_node = self.head
                    self.head.insert_before(node.value)
                    # self.head.next = prev_node
                    current.delete()

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if not self.tail or not self.tail.prev:
            return None

        while self.tail.prev is not None and self.tail.next is None:
            if node == self.tail.prev:
                node.delete()
                new_tail = ListNode(node)
                new_tail.insert_after(self.tail)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        pass

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next


if __name__ == '__main__':

    ll = DoublyLinkedList()
    ll.head = ListNode("A")
    second = ListNode("B")
    third = ListNode("C")

    ll.head.next = second
    second.next = third

    ll.move_to_front(second)

    ll.print_list()
