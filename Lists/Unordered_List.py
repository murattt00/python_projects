class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next

class UnorderedList:

    def __init__(self):
        self.head = None

    def empty(self):
        return bool(self.head == None)

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

#    def treversing(self):
#        current = self.head
#        while current != None:
#            # place to put code for current
#            current = current.get_next()

    def get_length(self):
        current = self.head
        counter = 0
        while None != current:
            counter += 1
            current = current.get_next()

    def get_item(self, pos):
        current = self.head
        counter = 0
        while None != current:
            if counter == pos:
                return current.get_data()
            counter += 1
            current = current.get_next()

    def search(self, item):
        current = self.head
        while None != current:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
    def remove(self, item):
        current = self.head
        pre = None
        while None != current:
            if current.get_data() == item:
                if None == pre:
                    self.head = current.get_next()
                else:
                    pre.set_next(current.get_next())
                return current.get_data()
            pre = current
            current = current.get_next()
        return None
    def add_order(self, item):
        current = self.head
        pre = None
        n = Node(item)
        stop = False
        while current != None and not stop:
            if item < current.get_data():
                stop = True
            else:
                pre = current
                current = current.get_next()
        if pre == None:
            n.set_next(self.head)
            self.head = n
        else:
            n.set_next(current)
            pre.set_next(n)
        return






