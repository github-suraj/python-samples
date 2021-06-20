class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"
        
class LinkedList(object):
    def __init__(self, data=None):
        self.head = None
        self.size = 0
        if data:
            self.extend(data)
        
    def isEmpty(self):
        return self.size == 0
        
    def getElements(self):
        elements = list()
        cur = self.head
        while cur:
            elements.append(cur.data)
            cur = cur.next
        return elements
    
    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.size += 1
        
    def appendleft(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            raise IndexError("Popping an emply list")
        last = self.head
        while last.next.next:
            last = last.next
        remove = last.next
        last.next = None
        self.size -= 1
        return remove.data
        
    def popleft(self):
        if self.isEmpty():
            raise IndexError("Popping an emply list")
        remove = self.head
        self.head = remove.next
        self.size -= 1
        return remove.data
        
    def extend(self, data):
        if isinstance(data, (list, tuple)):
            for d in data:
                self.append(d)
        else:
            raise TypeError(f"data can be a list/tuple, but found {type(data)}")
        
    def extendleft(self, data):
        if isinstance(data, (list, tuple)):
            for d in data:
                self.appendleft(d)
        else:
            raise TypeError(f"data can be a list/tuple, but found {type(data)}")
            
    def insert(self, idx, value):
        if idx >= self.size:
            raise IndexError("Index out of range")
        elif idx == 0:
            self.appendleft(value)
        else:
            node = Node(value)
            last = self.head
            while idx > 1:
                last = last.next
                idx -= 1
            node.next = last.next
            last.next = node
            self.size += 1
    
    def insert_after_value(self, after, value):
        last = self.head
        while last:
            if last.data == after:
                break
            last = last.next
        else:
            raise ValueError(f"{after} not in the list")
        node = Node(value)
        node.next = last.next
        last.next = node
        self.size += 1

    def remove(self, data):
        temp = self.head
        if temp:
            # If head node itself holds the key to be deleted
            if temp.data == data:
                self.head = temp.next
            else:
                # Search for the key to be deleted,
                # keep track of the previous node as we need to change 'prev.next'
                while temp:
                    if temp.data == data:
                        break
                    prev = temp
                    temp = temp.next
                else:
                    raise ValueError(f"{data} not in the list")
                prev.next = temp.next
            self.size -= 1
            temp = None
        else:
            raise ValueError(f"{data} not in the list")

    def remove_at_index(self, idx):
        if idx >= self.size:
            raise IndexError("Index out of range")
        elif idx == 0:
            self.popleft()
        else:
            temp = self.head
            while idx:
                prev = temp
                temp = temp.next
                idx -= 1
            prev.next = temp.next
            temp = None
            self.size -= 1

    def __len__(self):
        return self.size

    def __str__(self):
        return f"LinkedList({self.getElements()})"
