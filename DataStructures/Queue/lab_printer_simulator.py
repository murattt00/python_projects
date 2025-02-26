import random


class Queue():
    def __init__(self):
        self.items = []
    def isempty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

class Printer:
    def __init__(self,ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaning = 0
    def tick(self):
        if self.current_task is not None:
            self.time_remaning = self.time_remaning -1
            if self.time_remaning <= 0:
                self.current_task = None
    def busy(self):
        return self.current_task is not None
    def start_Next(self,new_task):
        self.current_task = new_task
        self.time_remaning = new_task.get_pages() * 60 / self.page_rate

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,50)

    def get_stamp(self):
        return self.timestamp
    def get_pages(self):
        return self.pages
    def wait_time(self,current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []
    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        if(not lab_printer.busy()) and (not print_queue.isempty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_Next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining" % (average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    return num == 180
for i in range(10):
    simulation(3600, 10)