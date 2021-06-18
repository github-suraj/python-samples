class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class Stack(object):
    '''Stack data structure using Linked List'''
    def __init__(self):
        self._head = None
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def getElements(self):
        elements = list()
        itr = self._head
        while itr:
            elements.append(itr.data)
            itr = itr.next
        return elements

    def push(self, data):
        node = Node(data)
        if self.isEmpty():
            self._head = node
        else:
            node.next = self._head
            self._head = node
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Poping the empty Stack')
        remove = self._head
        self._head = remove.next
        self.__size -= 1
        return remove.data

    def peak(self):
        if self.isEmpty():
            raise Exception('Peaking the empty Stack')
        return self._head.data

    def __str__(self):
        return f"Stack({self.getElements()})"
