class Queue():
    def __init__(self):
        self.items = []
    def isempty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


def Hotpatato(players: list , tur: int):
    Qplayers = Queue()
    for p in players:
        Qplayers.enqueue(p)
    while  Qplayers.size() > 1:
        for i in range(tur):
            top = Qplayers.dequeue()
            Qplayers.enqueue(top)
        Qplayers.dequeue()
    return Qplayers.dequeue()

print(Hotpatato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


