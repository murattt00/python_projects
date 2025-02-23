class BinaryTree:
    def __init__(self, val):
        self.key = val
        self.rightChild = None
        self.leftChild = None

    def get_root(self):
        return self.key

    def get_rightChild(self):
        return self.rightChild

    def get_leftChild(self):
        return self.leftChild

    def set_roof(self, obj):
        self.key = obj

    def insertLeft(self, newNode):
        oldLeft = self.leftChild
        self.leftChild = BinaryTree(newNode)
        self.leftChild.leftChild = oldLeft

    def insertRight(self, newNode):
        oldRight = self.rightChild
        self.rightChild = BinaryTree(newNode)
        self.rightChild.rightChild = oldRight




