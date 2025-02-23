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
