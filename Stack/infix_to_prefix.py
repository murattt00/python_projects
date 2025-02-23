class Stack():
    def __init__(self):
        self.items = []
    def isempty(self):
        return len(self.items) == 0
    def push(self, item):
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





def infix_to_prefix(String: str):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, ')': 1}
    op_Stack = Stack()
    token_list = String.split()[::-1]
    prefix = []
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTVWXYZ0123456789":
            prefix.insert(0, token)
        elif token == ")":
            op_Stack.push(token)
        elif token == "(":
            top = op_Stack.pop()
            while top != ")":
                prefix.insert(0, top)
                top = op_Stack.pop()
        else:
            if op_Stack.isempty():
                op_Stack.push(token)
            elif prec[token] <= prec[op_Stack.peek()]:
                prefix.insert(0, op_Stack.pop())
                op_Stack.push(token)
            else:
                op_Stack.push(token)
    while not op_Stack.isempty():
        prefix.insert(0, op_Stack.pop())
    return "".join(prefix)

print(infix_to_prefix("A * B * C * D + E + F"))
