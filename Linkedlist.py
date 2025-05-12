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


    def insert_at_index(self, index, data):
        if index < 0 or index >self.get_lenght():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_start(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def delete_at_index(self, index):
        if index< 0 or index>= self.get_lenght():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def search(self, value):
            itr = self.head
            index = 0
            while itr:
                if itr.data == value:
                    return index
                itr = itr.next
                index += 1
            return -1

if __name__ == '__main__':
        ll = LinkedList()
        ll.insert_at_start(5)
        ll.insert_at_start(69)
        ll.insert_at_end(10)
        ll.insert_at_end(156)
        ll.insert_at_index(0, 23)
        ll.display()
        print("Found at index:", ll.search(5))


