class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMin(self):
        return self.heap[0] if self.heap else None

    def removeMin(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.__minHeapify(0)
        return min_val

    def __percolateUp(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def __minHeapify(self, index):
        size = len(self.heap)

        while index < size:
            left = (index * 2) + 1
            right = (index * 2) + 2
            smallest = index

            if left < size and self.heap[smallest] > self.heap[left]:
                smallest = left
            if right < size and self.heap[smallest] > self.heap[right]:
                smallest = right
            if smallest != index:
                self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
                index = smallest
            else:
                break

    def buildHeap(self, arr):
        self.heap = arr[:]
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.__minHeapify(i)
