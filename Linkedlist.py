class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count