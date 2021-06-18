class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class Queue(object):
    '''Queue data structure prototype'''
    def __init__(self):
        self._front = self._rear = None
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def getElements(self):
        elements = list()
        itr = self._front
        while itr:
            elements.append(itr.data)
            itr = itr.next
        return elements

    def enQueue(self, data):
        node = Node(data)
        if self._rear == None:
            self._front = self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self.__size += 1

    def deQueue(self):
        if self.isEmpty():
            raise Exception('Poping the Empty Queue')
        remove = self._front
        self._front = remove.next
        if self._front == None:
            self._rear = None
        self.__size -= 1
        return remove.data

    def first(self):
        if self.isEmpty():
            raise Exception('Fetching first of the empty Queue')
        return self._front.data

    def __str__(self):
        return f"Queue({self.getElements()})"
