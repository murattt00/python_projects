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


def infix_to_postfix(String: str):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    remainder = Stack()
    postfixlist = []
    infixlist = String.split()
    postfix = ""
    for i in infixlist:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfixlist.append(i)
        elif( i == "("):
            remainder.push(i)
        elif(i == ")"):
            while remainder.peek() != "(":
                postfixlist.append(remainder.pop())
            remainder.pop()
        else:
            if remainder.isempty():
                remainder.push(i)
            elif(prec[i] <= prec[remainder.peek()]):
                postfixlist.append(remainder.pop())
                remainder.push(i)
            else:
                remainder.push(i)

    for i in postfixlist:
        postfix += i
    while not remainder.isempty():
        postfix += remainder.pop()

    return postfix


print(infix_to_postfix("A + ( ( B + C ) * ( D + E ) )"))








