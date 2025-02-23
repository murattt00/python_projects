from çalışma.Queue import Queue


def Hotpatato(players : list,tur : int):
    Qplayers = Queue
    for p in players:
        Qplayers.enqueue(p)
    while  Qplayers.size() > 1:
        for i in range(tur):
            top = Qplayers.dequeue()
            Qplayers.enqueue(top)
        Qplayers.dequeue()
    return Qplayers.dequeue()

print(Hotpatato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


