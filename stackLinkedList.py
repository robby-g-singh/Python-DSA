class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
        else:
            curr_head = self.head
            self.head = temp
            temp.next = curr_head

    def pop(self):
        if self.head is None:
            print("List is empty!")
            return -1
        else:
            curr_head = self.head
            if curr_head.next is None:
                self.head = None
            else:
                new_head = curr_head.next
                self.head = new_head
            return curr_head

    def peek(self):
        if self.head is None:
            print("List is empty!")
            return -1
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count

    def print_list(self):
        temp = self.head

        if temp is None:
            print("List is empty!")

        elif temp.next is None:
            print(temp.data)

        else:
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")
