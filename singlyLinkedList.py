# Linked List implementation
# functions to implement: prepend, append, search, delete, print

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):  # returns the Head Node O(1)
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # checks whether Head node is null, i.e., list is empty O(1)
            return True
        return False

    def prepend(self, val):
        new_head = Node(val)
        if self.head_node is None:
            self.head_node = new_head
        else:
            new_head.next_element = self.head_node
            self.head_node = new_head

    def append(self, val):
        temp = Node(val)
        if self.head_node is None:
            self.head_node = temp
        else:
            last = self.head_node
            while last.next_element:
                last = last.next_element
            last.next_element = temp

    def remove_head(self):
        if self.head_node is None:
            print("List is empty, cannot perform!")
        else:
            self.head_node = self.head_node.next_element

    def reverse(self):
        current = self.head_node
        prev = None

        while current:
            forward = current.next_element  # store the next element of the current node
            current.next_element = prev  # swap out next pointer to point to the previous node
            prev = current  # update prev to be one node forward
            current = forward  # update the current node to be one node forward
        self.head_node = prev

    def print_list(self):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.head_node
            while temp.next_element is not None:
                print(temp.data, end=" -> ")
                temp = temp.next_element
            print(temp.data, " -> None")


first = LinkedList()
second = LinkedList()
lst = LinkedList()


second.append(2)
second.append(3)
second.append(4)
second.append(5)

first.print_list()
