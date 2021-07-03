class HashTable(object):
    def __init__(self, size=10):
        self.MAX = size
        self.table = [list() for _ in range(self.MAX)]
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def keys(self):
        keys = list()
        for elements in self.table:
            if elements:
                for element in elements:
                    keys.append(element[0])
        return keys

    def values(self):
        values = list()
        for elements in self.table:
            if elements:
                for element in elements:
                    values.append(element[1])
        return values

    def items(self):
        items = list()
        for elements in self.table:
            if elements:
                for element in elements:
                    items.append(element)
        return items

    def __setitem__(self, key, value):
        h = hash(key) % self.MAX
        for idx, mapping in enumerate(self.table[h]):
            if mapping[0] == key:
                self.table[h][idx] = (key, value)
                break
        else:
            self.table[h].append((key, value))
            self.size += 1

    def __getitem__(self, key):
        h = hash(key) % self.MAX
        for mapping in self.table[h]:
            if mapping[0] == key:
                return mapping[1]

    def __delitem__(self, key):
        h = hash(key) % self.MAX
        for idx, mapping in enumerate(self.table[h]):
            if mapping[0] == key:
                del self.table[h][idx]
                self.size -= 1

    def __len__(self):
        return self.size

    def __str__(self):
        return f"HashTable({self.items()})"
