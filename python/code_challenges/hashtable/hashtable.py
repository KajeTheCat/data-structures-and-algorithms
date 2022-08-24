hello = "world"

class Node:
    """
    Node class
    """

    def __init__(self, value, key, next = None):
        self.next = next
        self.value = value
        self.key = key

class Hashtable:
    """
    Hashtable contains the methods for set, get, contains, keys, and hash.
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def _set(self, key, value):
        # This method should hash the key and add the key and value pair to the table, handling collisions as needed
        key = str(key)
        index = self.hash(key)
        node = Node(value, key)

        if self._buckets[index] != None:
            node.next = self._buckets[index]
        self._buckets[index] = node

    def get(self, key):
        # Returns: value associated with that key in the table
        key = str(key)
        index = self.hash(key)

        if self._buckets[index] != None:
            current = self._buckets[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            return "Could not find value"

    def contains(self, key):
        # Returns boolean, indicating if the key exists in the table already
        key = str(key)
        index = self.hash(key)

        if self._buckets[index] != None:
            current = self._buckets[index]
            while current:
                if current.key == key:
                    return True
                current = current.next
            return False

    def keys(self):
        # returns collection of keys
        key_list = []
        for key in self._buckets:
            if key != None:
                current = key
                while current:
                    key_list.append(current.key)
                    current = current.next
        return key_list

    def hash(self, key):
        total = 0

        for letter in key:
            total += ord(letter)

        primed = total * 13
        index = primed % self.size

        return index

if __name__ == "__main__":

    h = Hashtable(10)
    print(h.hash("a"))
    h._set("ape", 1)
    h._set("bow", 2)
    h._set("cat", 3)
    h._set("pea", 4)
    # print(h._buckets)
    # for value in h._buckets:
    #     if value != None:
    #         current = value
    #         while current:
    #             print(current.key, current.value)
    #             current = current.next
    # print(h.get("ape"))
    # print(h.contains("ape"))
    print(h.keys())
