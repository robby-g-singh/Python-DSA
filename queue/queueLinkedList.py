class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def front(self):
        return self.head.data

    def rear(self):
        return self.tail.data

    def size(self):
        return self.count

    def enqueue(self, element):
        temp = Node(element)

        if self.is_empty():
            self.head = self.tail = temp

        else:
            curr_tail = self.tail
            curr_tail.next = temp
            self.tail = temp

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Cannot dequeue from an empty queue!")
            return -1
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None

        self.count -= 1
        return data

    def print_queue(self):
        if self.is_empty():
            print("Empty queue!")
            return -1
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

