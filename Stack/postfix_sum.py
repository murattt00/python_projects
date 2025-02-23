class Stack():
    def __init__(self):
        self.items = []
    def isempty(self):
        return len(self.items) == 0
    def push (self, item):
            self.items.append(item)
    def pop(self):
        if not self.isempty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.isempty():
            return self.items[-1]
        return None
    def size(self):
        return len(self.items)


def postfix_sum(expression: str):
    val_stack = Stack()
    ex_list = expression.split()
    for token in ex_list:
        if token not in "*/+-":
            val_stack.push(int(token))
        else:
            op2 = val_stack.pop()
            op1 = val_stack.pop()
            