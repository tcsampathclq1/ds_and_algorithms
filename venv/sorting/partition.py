def partition_two_pointers_left(arr):
    left = 1
    right = len(arr) - 1
    key = arr[0]
    while left < right:
        while left < len(arr) and arr[left] <= key:
            left += 1
        while right >= 0 and arr[right] > key:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    arr[right], arr[0] = arr[0], arr[right]
    return right

def partition_two_pointers_right(arr):
    last = len(arr) - 1
    key = arr[last]
    left = 0
    right = arr[last - 1]

    while right > left:
        while right >= 0 and arr[right] > key:
            right -= 1
        while left <= last and arr[left] <= key:
            left -= 1
        if right > left:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            left += 1
    arr[left], arr[last] = arr[last], arr[left]
    return left

def partition_one_pointer_left(arr):
    key = arr[0]
    pivot = 0
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
    print("Initial Array " + str(arr))
    pivot = partition_two_pointers_left(arr)
    print("Two Pointer Partitioned Array Left Pivot" + str(arr))
    print("Pivot element is " + str(pivot))

    arr = [17, 7, 27, 15, 111, 25]
    pivot = partition_one_pointer_right(arr)
    print("One Pointer Partitioned Array Right Pivot" + str(arr))
    print("Pivot element is " + str(pivot))

    arr = [17, 7, 27, 15, 111, 25]
    pivot = partition_one_pointer_left(arr)
    print("One Pointer Partitioned Array Left Pivot" + str(arr))
    print("Pivot element is " + str(pivot))

    arr = [17, 7, 27, 15, 111, 25]
    pivot = partition_one_pointer_right(arr)
    print("One Pointer Partitioned Array Right Pivot" + str(arr))
    print("Pivot element is " + str(pivot))

if __name__ == "__main__":
    main()