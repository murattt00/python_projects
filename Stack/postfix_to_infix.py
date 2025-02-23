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

def postfix_to_infix(expession: str):
    val_Stack = Stack()
    ex_list = expession.split()
    for token in ex_list:
        if token in "ABCDEFGHIJKLMNOPQRSTVWXYZ0123456789":
            val_Stack.push(token)
        else:
            op2 = val_Stack.pop()
            op1 = val_Stack.pop()
            new_ex = "(" + op1 + token + op2 + ")"
            val_Stack.push(new_ex)
    return val_Stack.pop()
print(postfix_to_infix("A B + C * D E - F G + * -"))