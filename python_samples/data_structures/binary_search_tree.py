class BinarySearchTree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def isEmpty(self):
        return self == None

    def insert(self, data):
        if self.data == data:
            return
        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)
        self.size += 1

    def search(self, value):
        if self.data == value:
            return True
        if self.data > value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def delete(self, value):
        if self.search(value):
            if self.data > value:
                if self.left:
                    self.left = self.left.delete(value)
            elif self.data < value:
                if self.right:
                    self.right = self.right.delete(value)
            else:
                if self.left == None and self.right == None:
                    return None
                elif self.left == None:
                    return self.right
                elif self.right == None:
                    return self.left

                min = self.right.findMin()
                self.data = min
                self.right = self.right.delete(min)
            self.size -= 1
        return self

    def inorderTree(self):
        elements = list()
        if self.left:
            elements += self.left.inorderTree()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorderTree()
        return elements

    def preorderTree(self):
        elements = list()
        elements.append(self.data)
        if self.left:
            elements += self.left.preorderTree()
        if self.right:
            elements += self.right.preorderTree()
        return elements

    def postorderTree(self):
        elements = list()
        if self.left:
            elements += self.left.postorderTree()
        if self.right:
            elements += self.right.postorderTree()
        elements.append(self.data)
        return elements

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data

    def findMax(self):
        if self.right:
            return self.right.findMax()
        return self.data

    def treeSum(self):
        sum = 0
        sum += self.data
        if self.left:
            sum += self.left.treeSum()
        if self.right:
            sum += self.right.treeSum()
        return sum

    def __len__(self):
        return self.size

    def __str__(self):
        return f"BinarySearchTree({self.inorderTree()})"
