# arr = [2, 66, 30, 5, 9, 10]
# n = len(arr)

# def maxheap():
#     for i in range(n//2-1, -1, -1):
#         largest_subtree = reassign_largest(i)
#         swap(i, largest_subtree)
#     print(arr)


# def reassign_largest(i):
#     largest = i # largest
#     l = 2*i + 1 # left
#     r = 2*i + 2 # right
#     if (r <= n-1): # greater value, can give error: 'list index out of range'
#         if arr[r] > arr[largest]:
#             largest = reassign_largest(r)
#         elif arr[l] > arr[largest]:
#             largest = reassign_largest(l)
#     elif (l<=n-1 and r>n-1):
#         if arr[l] > arr[largest]:
#             largest = reassign_largest(l)
#     return largest

# def swap(i, largest_subtree):
#     temp = arr[i]
#     arr[i] = arr[largest_subtree]
#     arr[largest_subtree] = temp

# maxheap()

## this was my implementation with ofcourse being errory & lengthy

arr = [2, 66, 30, 5, 9, 10]
n = len(arr)

def maxheap():
    # Build a maxheap.
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)
    # print(arr)

def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # Check if left child of root exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # Check if right child of root exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root again as it can be smaller than its children
        max_heapify(arr, n, largest)

def maxheap_sort():
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        max_heapify(arr, i, 0)


maxheap()
maxheap_sort()
print("sorted maxheap: ", arr)