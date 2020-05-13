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
            self.head.prev = new_node
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
            self.tail.next = new_node
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

            while current is not None:  # traverse through list
                print(f"loop", current.value)
                current = current.next
                if current == node:  # stop at node to remove and move
                    print(f"first print", current.value)
                    break
            # print(f"current after break", current.prev.value)
            # removes node from current spot and links prev/next together
            current.delete()
            print(f"current", current.value)
            self.add_to_head(node.value)  # inserts node in front
            self.length -= 1

            # current_node = node
            # node.delete()
            # self.length -= 1
            # self.add_to_head(current_node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):

        # if not self.head and not self.tail:
        #     return None

        # else:

        #     current = self.head

        #     while current is not None:
        #         if current == node:
        #             break
        #         current = current.next

        #     print(f"current", current.value)
        #     current.delete()  # WHY won't this delete?!
        #     self.add_to_tail(node.value)
        #     self.length -= 1

        current_node = node
        if current_node.prev is None:
            self.head = current_node.next

        node.delete()
        self.length -= 1
        self.add_to_tail(current_node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # think about edge cases, what if you remove tail, what if you remove head, what if length is one, what if empty, etc
        if not self.head and not self.tail:
            return None

        elif node.prev is None and node.next is None:
            self.head = None
            self.tail = None
            self.length -= 1

        elif not node.prev:
            self.head = node.next
            node.delete()
            self.length -= 1
            return node.value
            # self.remove_from_head() not working with line 140 in test

        elif not node.next:
            self.remove_from_tail()

        else:
            node.delete()
            self.length -= 1
            return node.value

    """Returns the highest value currently in the list"""

    def get_max(self):
        current = self.head
        max_num = current.value
        while current.next is not None:
            if max_num < current.next.value:
                max_num = current.next.value

            current = current.next

        return max_num

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next


if __name__ == '__main__':

    ll = DoublyLinkedList()
    ll.add_to_head("A")
    ll.add_to_tail("B")
    ll.add_to_tail("C")

    ll.move_to_end(ll.head)

    ll.print_list()
