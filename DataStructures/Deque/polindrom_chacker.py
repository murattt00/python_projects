class Deque:
    def __init__(self):
        self.items = []

    def isempty(self):
        return not bool(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rare(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rare(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def polindrom_checker(string: str):
    deQ = Deque()
    for i in string.lower():
        deQ.add_rare(i)
    while deQ.size() > 1:
        if deQ.remove_rare() != deQ.remove_front():
            return False
    return True

print(polindrom_checker("RAdar"))