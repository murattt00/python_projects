# Verilen sınıfların tanımı
class Node:
    def _init_(self, data=None):
        self.data = data
        self.next = None

class Linked_list:
    def _init_(self):
        self.head = Node()
        self.tail = self.head

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    def get(self, index):
        if index >= self.length():
            print("ERROR! 'Get' index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

def sorted_list(list1,list2):
    # Yeni bir birleşik liste oluşturma
    combined_elements = []
    # my_list ve your_list'teki elemanları sırayla combined_elements listesine ekleme
    for i in range(list1.length()):
        combined_elements.append(list1.get(i))

    for i in range(list2.length()):
        combined_elements.append(list2.get(i))

    # Elemanları sıralama
    combined_elements.sort()

    # Sıralanmış elemanlarla yeni bir Linked_list oluşturma
    sorted_list = Linked_list()

    for elem in combined_elements:
        sorted_list.append(elem)

    # Sıralanmış listeyi ekrana yazdırma
    sorted_list.display()



# my_list ve your_list oluşturma
my_list = Linked_list()
your_list = Linked_list()

# my_list'e 1, 2, 3, 4, 5 ekleyelim
for i in [1, 2, 3, 4, 5]:
    my_list.append(i)

# your_list'e 2, 8 ekleyelim
for i in [2, 8]:
    your_list.append(i)
