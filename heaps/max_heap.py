class MaxHeap:
    def __init__(self):  # define the heap, initialize with emtpy list
        self.heap = []

    def insert(self, val):  # add a new element to the end of a heap, making it a new leaf node.
        # then call the percolateUp function on it to maintain the heap property
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMax(self):  # O(1) operation, returns the first item in the heap
        return self.heap[0] if self.heap else None

    def removeMax(self):  # start off with simple base cases of heap length being 0 or 1
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # if the heap is greater than 1:
        max_val = self.heap[0]  # keep track of the current max we want to remove
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # swap the root node with the last one in the heap
        self.heap.pop()  # pop the last element in the node, i.e. our newly swapped previous max
        self.__maxHeapify(0)  # call maxHeapify on our new root, to restore the heap property
        return max_val  # return the value of the previous root

    def __percolateUp(self, index):  # works its way up the heap from a given index
        while index > 0:
            parent = (index - 1) // 2  # standard formula to find the parent of a node at a given index

            if self.heap[parent] < self.heap[index]:  # if the parent < child, that violates the heap property,
                # so you perform a swap:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent  # update the index to the parent, to work upwards until index == 0
            else:
                break  # break the loop if the parent > child

    def __maxHeapify(self, index):  # works its way down a heap from a given index
        size = len(self.heap)

        while index < size:
            # standard formulas to find the left and right children of a node at a given index
            left = (index * 2) + 1
            right = (index * 2) + 2
            largest = index  # set a variable to keep track of the index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left  # keep track of the index of where the left child is greater than its parent

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right  # keep track of the index of where the right child is greater than its parent

            if largest != index:  # if the largest variable was updated, that means one of the above cases was True,
                # therefore we swap:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest  # update the index variable to continue working down the heap

            else:
                break  # break the loop if none of the above conditions were met, i.e. heap property is in tact

    def buildHeap(self, arr):
        self.heap = arr[:]  # use a shallow copy to prevent changes to the original
        # parameters: start at last non-leaf node; continue until i == 0; iterate backwards:
        for i in range(len(arr)//2 - 1, -1, -1):
            self.__maxHeapify(i)


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMax())
