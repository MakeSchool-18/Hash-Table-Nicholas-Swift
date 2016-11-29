#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # TODO: append given item
        node = Node(item)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail.next.previous = self.tail
            self.tail = node
        return

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        node = Node(item)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.head.next.previous = self.head
        return True

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found

        if self.head is None:
            raise ValueError('Cannot delete from empty Linked List')

        current = self.head

        # If item is first!
        if current.data == item:
            if current.next is not None:
                self.head = current.next
                self.head.previous = None
            else:
                self.head = None
                self.tail = None
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
                return
            current = current.next

        raise ValueError('Cannot delete this element from the linked list')

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        current = self.head
        while current is not None:
            if quality(current.data) == True:
                return current.data
            current = current.next
        return None

    def __contains__(self, item):
        """Does it contain the item"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next


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
    for item in ll:
        print("prev: ", item.previous)
        print("item: ", item)
        print("next: ", item.next)
        print("\n")


if __name__ == '__main__':
    test_linked_list()