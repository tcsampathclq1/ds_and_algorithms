def selection_sort(arr, reverse=False):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if (not reverse and arr[j] < arr[min_index]) or (reverse and arr[j] > arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    arr = [-5, 6, 9, 3, 2, 0, 3, 87, 55]
    print(arr)
    selection_sort(arr)
    print(arr)
    arr = [-5, 6, 9, 3, 2, 0, 3, 87, 55]
    print(arr)
    selection_sort(arr, True)
    print(arr)


if __name__ == "__main__":
    main()