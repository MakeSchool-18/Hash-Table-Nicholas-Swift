#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        # Best: Omega(1)
        # Worst: O(1)

        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        # Best: Omega(n)
        # Worst: O(n)

        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        # Best: Omega(n) (because of .as_list())
        # Worst: O(n)

        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        # Best: Omega(n)
        # Worst: O(n) 

        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        # Best: Omega(1)
        # Worst: O(1)

        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # Best: Omega(1)
        # Worst: O(1)

        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # Best: Omega(1)
        # Worst: O(1)

        node = Node(item)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail.next.previous = self.tail
            self.tail = node

        self.size += 1
        return

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # Best: Omega(1)
        # Worst: O(1)

        node = Node(item)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.head.next.previous = self.head

        self.size += 1
        return True

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # Best: Omega(1)
        # Worst: O(n)

        if self.head is None:
            raise ValueError('Cannot delete from empty Linked List')

        current = self.head

        # If item is first!
        if current.data == item:
            self.head.previous = None
            self.head = current.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        while current.next is not None:
            if current.next.data == item:
                newNext = current.next.next
                if newNext is not None:
                    current.next = newNext
                    current.next.previous = current
                else:
                    current.next = None
                    self.tail = current
                self.size -= 1
                return
            current = current.next

        raise ValueError('Cannot delete this element from the linked list')

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # Best: Omega(1)
        # Worst: O(n)

        current = self.head
        while current is not None:
            if quality(current.data) is True: # Need to be explicit or not??????
                return current.data
            current = current.next
        return None

    # def replace(self, item, new_item):
    #     """Replace the item with the new item"""
    #     # Best: Omega(1)
    #     # Worst: O(n)

    #     current = self.head
    #     while current is not None:
    #         if item == current.data:
    #             current.data = new_item
    #             return
    #         current = current.next
    #     #raise ValueError('The item does not exist in the linked list')
    #     return

    def __contains__(self, item):
        """Does it contain the item"""
        # Best: Omega(1)
        # Worst: O(n)

        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self):
        """Iterate through all items"""
        # Best: Omega(1)
        # Worst: O(1)

        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        """Get the length of the linked list"""
        # Best: Omega(1)
        # Worst: O(1)

        return self.length()
        # return self.size

    def __nonzero__(self):
        """Will the linked list equate to false"""
        # Best: Omega(1)
        # Worst: O(1)

        return not self.is_empty()


def test_linked_list():
    # Test appending
    print("Testing Appending")
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    # Test deleteing
    print("Testing Deleting")
    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    # Test iterable
    print("Testing Iterable")
    ll.append('a')
    ll.append('b')
    ll.append('c')
    ll.append('wow')


if __name__ == '__main__':
    test_linked_list()