class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def print_list(self):
        if self.is_empty():
            print("List is empty!")
        else:
            temp = self.head
            while temp:
                if temp is self.head:
                    print(str(temp.data), end=" -> ")
                else:
                    print("<- " + str(temp.data), end=" -> ")
                temp = temp.next
            print("None")

    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current_head = self.head
            current_head.prev = new_node
            new_node.next = current_head
            self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            last_element = temp
            last_element.next = new_node
            new_node.prev = last_element

    def insert(self, index, data):
        new_node = Node(data)
        count = 0

        if self.is_empty():
            print("List is empty, adding to the head...")
            self.head = new_node
        else:
            temp = self.head
            while temp:
                if count == index:
                    curr_prev = temp.prev
                    curr_prev.next = new_node
                    new_node.prev = curr_prev
                    new_node.next = temp
                    temp.prev = new_node

                temp = temp.next
                count += 1
            if index > count:
                return -1

    def remove_head(self):
        if self.is_empty():
            print("Cannot remove from an empty list!")
        else:
            if self.head.next is None:
                self.head = None
            else:
                new_head = self.head.next
                self.head = new_head
                new_head.prev = None

    def remove_tail(self):
        if self.is_empty():
            print("Cannot remove from an empty list!")
        else:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp:
                    if temp.next is None:
                        new_tail = temp.prev
                        new_tail.next = None
                    temp = temp.next

    def remove_at_index(self, index):
        if self.is_empty():
            print("Cannot remove from an empty list!")
        else:
            count = 0
            temp = self.head

            while temp:
                if index == 0:
                    self.remove_head()
                elif (count == index) and (temp.next is None):
                    self.remove_tail()
                else:
                    if count == index:
                        # prev -> <- current -> <- next
                        prev_element = temp.prev
                        next_element = temp.next
                        prev_element.next = next_element
                        next_element.prev = prev_element
                count += 1
                temp = temp.next

    def search(self, val):
        if self.is_empty():
            print("Cannot search an empty list!")
        else:
            temp = self.head
            count = 0
            while temp:
                if temp.data == val:
                    print(f"Found value {val} at Node {count}")
                    return True
                count += 1
                temp = temp.next
        return False


test = DoublyLinkedList()
test.prepend(1)
# test.print_list()
test.prepend(2)
test.prepend(3)

test.append(6)
test.append(10)
test.insert(1, 12)
test.print_list()
test.search(6)
