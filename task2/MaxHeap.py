class MaxHeap:
    def __init__(self):
        # Internal list representation of the heap.
        # In a max-heap, each parent node is >= its children.
        self.heap = []

    def _heapify_down(self, index):  # index: the node to be sifted down
        # Restore the max-heap property by moving the value at `index`
        # down the tree until it is >= both children (or it reaches a leaf).
        size = len(self.heap)

        largest = index  # assume the current node is the largest initially

        # Compute indices of left and right children in an array-based heap
        left = 2 * index + 1
        right = 2 * index + 2

        # If left child exists and is greater than current largest, update largest
        if left < size and self.heap[left] > self.heap[largest]:
            largest = left

        # If right child exists and is greater than current largest, update largest
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        # If one of the children is larger, swap and continue heapifying down
        if largest != index:
            self.heap[largest], self.heap[index] = \
            self.heap[index], self.heap[largest]

            # Continue sifting down from the child position where the swap occurred
            self._heapify_down(largest)

    def _heapify_up(self, index):
        # Restore the max-heap property by moving the value at `index`
        # up the tree while it is greater than its parent.
        parent = (index - 1) // 2  # parent index in an array-based heap

        # If not at root and parent is smaller, swap with parent
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = \
            self.heap[index], self.heap[parent]

            # Continue sifting up from the parent's position
            self._heapify_up(parent)

    def insert(self, value):
        # Add a new value to the heap, then restore heap property by heapifying up.
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        # Remove and return the maximum element (root of the heap).
        # Steps:
        # 1) Swap root with last element
        # 2) Pop last element (former root)
        # 3) Heapify down from root to restore max-heap property
        if len(self.heap) == 0:
            # Return False to indicate the heap is empty (no max to extract)
            return False

        # Swap the root (max) with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        # Remove the last element (which is the max after the swap)
        max_val = self.heap.pop()

        # Restore the heap property starting from the root
        self._heapify_down(0)

        # Return the extracted maximum value
        return max_val

    def build_heap(self, array):
        # Build a max-heap from an arbitrary array in O(n) time using bottom-up heapify.
        # Copy to avoid modifying the original input array.
        self.heap = array[:]

        # Start from the last non-leaf node and heapify down each node to the root.
        # Last non-leaf node is at index (n // 2 - 1).
        start = len(self.heap) // 2 - 1
        for i in range(start, -1, -1):
            self._heapify_down(i)
