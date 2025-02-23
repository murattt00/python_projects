class Double_Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_pre(self):
        return self.pre
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next
    def set_pre(self, pre):
        self.pre = pre

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Bir önceki düğümü işaret eder

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Listenin başını tutar

    def is_empty(self):
        return self.head is None

    def add_to_front(self, data):
        """Listenin başına düğüm ekler."""
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def add_to_end(self, data):
        """Listenin sonuna düğüm ekler."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self, data):
        """Belirtilen değere sahip düğümü siler."""
        if self.head is None:
            print("Liste boş, silinecek eleman yok.")
            return

        current = self.head

        # Silinecek düğüm başta ise
        if current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        # Silinecek düğümü bul
        while current and current.data != data:
            current = current.next

        # Eğer düğüm bulunamadıysa
        if current is None:
            print("Eleman listede bulunamadı.")
            return

        # Düğümü listeden çıkar
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def traverse_forward(self):
        """İleri yönde listeyi yazdırır."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Geri yönde listeyi yazdırır."""
        current = self.head
        if not current:
            print("Liste boş.")
            return

        # Sona kadar git
        while current.next:
            current = current.next

        # Şimdi sondan başa doğru yazdır
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


