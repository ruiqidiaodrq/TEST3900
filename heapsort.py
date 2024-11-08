def heap_sort(arr):
    # Function to adjust the heap and maintain the heap property
    def heapify(arr, n, i):
        largest = i  # Initialize as root
        left = 2 * i + 1  # Left child
        right = 2 * i + 2  # Right child

        # If left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child exists and is greater than the current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest is not the root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            heapify(arr, n, largest)  # Recursively adjust the affected subtree

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the current end
        heapify(arr, i, 0)  # Adjust the heap, excluding the sorted part

    return arr

# Test code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = heap_sort(arr)
    print("Sorted array:", sorted_arr)
