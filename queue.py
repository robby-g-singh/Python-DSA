class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)


queue_test = Queue()
queue_test.enqueue(1)
queue_test.enqueue(2)
queue_test.enqueue(3)
queue_test.enqueue(4)
queue_test.enqueue(5)

print(queue_test.queue)

queue_test.dequeue()

print(queue_test.queue)
