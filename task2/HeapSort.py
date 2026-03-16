import random  # used only for generating a random test array

"""
STEP1: Build a Max-Heap from the unsorted array.
STEP2: Repeatedly extract the maximum and place it at the end of the array.

Heapsort idea (in-place):
- First rearrange the list into a max-heap (largest element at index 0).
- Then repeatedly swap the root (max) with the last element of the unsorted portion,
  shrink the unsorted portion by 1, and restore the heap property.
"""

def HeapSort(array):
    # Sorts `array` in ascending order in-place using heapsort.
    n = len(array)

    # STEP1: Build a Max-Heap from the unsorted array.
    # Start from the last non-leaf node and heapify down each node up to the root.
    # Indices from n//2 to n-1 are leaves, so we start at n//2 - 1.
    for i in range(n // 2 - 1, -1, -1):  # heapify starts from the last non-leaf node, all the way up
        _heapify(array, n, i)

    # STEP2: Repeatedly extract the maximum and place it at the end of the array.
    # At each iteration:
    # - array[0] is the maximum in the current heap.
    # - swap it with array[i] (end of the current unsorted region).
    # - heapify the reduced heap [0 .. i-1].
    for i in range(n - 1, 0, -1):
        array[0], array[i] = \
        array[i], array[0]  # move current max to its final position at the end
        _heapify(array, i, 0)  # restore max-heap property for the reduced heap

# index: the starting point
# this is a sifting down function
def _heapify(array, length, index):  # the underscore denotes it is intended for internal use by HeapSort()
    # Ensures the subtree rooted at `index` obeys the max-heap property,
    # assuming its children subtrees are already heaps.
    largest = index  # assume root is largest initially

    # Compute child indices in array-based heap representation
    left = 2 * index + 1  # get the left child by formula
    right = 2 * index + 2  # get the right child by formula

    # Find the largest among node at `index` and its (existing) children
    if left < length and array[left] > array[largest]:
        largest = left
    if right < length and array[right] > array[largest]:
        largest = right

    # If a child is larger than the current node, swap and continue sifting down
    if largest != index:
        array[largest], array[index] = \
        array[index], array[largest]
        _heapify(array, length, largest)  # continue to sift down from where the swap occurred

# Test
if __name__ == "__main__":
    # Create a random array of 10 integers between 0 and 100
    array = [random.randint(0, 100) for _ in range(10)]
    print("Before sorting:", array)

    # Perform heapsort (in-place)
    HeapSort(array)
    print("After sorting:", array)

# time complexity: O(nlogn) in all cases, because we have to build the Max-Heap first, which takes O(n),
# and then we have to extract the maximum n times, which takes O(logn) each time.
# space complexity: O(1) because we are sorting the array in place, and we are not using any extra space.
