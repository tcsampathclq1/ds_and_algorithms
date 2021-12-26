def partition_two_pointers(arr):
    left = 1
    right = len(arr) - 1
    pivot_val = arr[0]
    while left < right:
        while left < len(arr) and arr[left] <= pivot_val:
            left += 1
        while right >= 0 and arr[right] > pivot_val :
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    arr[right], arr[0] = arr[0], arr[right]
    return right

def partition_one_pointer_left(arr):
    key = arr[0]
    pivot = 0
    print(len(arr))
    for i in range(1, len(arr)):
        if arr[i] <= key:
            pivot += 1
            arr[pivot], arr[i] = arr[i], arr[pivot]
    arr[pivot], arr[0] = arr[0], arr[pivot]
    return pivot

def partition_one_pointer_right(arr):
    pivot = len(arr) - 1
    key = arr[pivot]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > key:
            pivot -= 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[len(arr) - 1] = arr[len(arr) - 1], arr[pivot]
    return pivot

def main():
    arr = [17,7, 27, 15, 111, 25]
    print(arr)
    pivot = partition_two_pointers(arr)
    print("Two Pointer Partitioned Array " + str(arr))
    print("Pivot element is " + str(pivot))
    arr = [17, 7, 27, 15, 111, 25]
    pivot = partition_one_pointer_left(arr)
    print("One Pointer Partitioned Array " + str(arr))
    print("Pivot element is " + str(pivot))
    arr = [17, 7, 27, 15, 111, 25]
    pivot = partition_one_pointer_right(arr)
    print("One Pointer Partitioned Array " + str(arr))
    print("Pivot element is " + str(pivot))

if __name__ == "__main__":
    main()