#!python#

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""

        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""

        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""

        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""

        num = 0
        for i in self.buckets:
            num += i.length()
        return num

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""

        for bucket in self.buckets:
            for node in bucket:
                if key == node.data[0]:
                    return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""

        # Find bucket
        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]

        # Check if key is already in bucket
        for node in bucket:
            if key == node.data[0]:
                return node.data[1]

        raise KeyError('Key is not in HashTable')

    def set(self, key, value):
        """Insert or update the given key with its associated value"""

        # Find bucket
        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]

        # Check if key is already in bucket
        for i, node in enumerate(bucket):
            if key == node.data[0]:
                new_tuple = (node.data[0], value)
                node.data = new_tuple
                return

        # Add new key, value to bucket
        bucket.append((key, value))
        return

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""

        # Find bucket
        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]

        # Check if key is in bucket
        for node in bucket:
            if key == node.data[0]:
                bucket.delete(node.data)
                return

        # Raise error if not found
        raise KeyError('Key is not in HashTable')

    def keys(self):
        """Return a list of all keys in this hash table"""

        keys = []
        for ll in self.buckets:
            for node in ll:
                keys.append(node.data[0])
        return keys

    def values(self):
        """Return a list of all values in this hash table"""

        values = []
        for ll in self.buckets:
            for node in ll:
                values.append(node.data[1])
        return values


if __name__ == '__main__':
    ht = HashTable()
    ht.set('one', 1)
    ht.set('two', 2)
    ht.set('three', 3)
    ht.set('two', 5)
    print(ht.keys())
    print(ht.values())


