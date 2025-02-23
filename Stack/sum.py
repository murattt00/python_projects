class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):  # o(1)
        return len(self.items) == 0
    def push(self, item):  # o(1)
        self.items.append(item)
    def pop(self):   # o(1)
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):  # o(1)
        if not self.is_empty():
            return self.items[-1]
        return None
    def size(self):
        return len(self.items)  # o(1)

def sum(my_stack: Stack()):
    sum = 0
    alist = []
    while not my_stack.is_empty():
        alist.insert(0, my_stack.pop())
    for i in alist:
        sum = sum + i
        my_stack.push(i)
    return sum
a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)
a.push(7)
a.push(8)
a.push(9)
print(a.items)
print(sum(a))
print(a.items)