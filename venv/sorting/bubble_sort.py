def bubble_sort(arr, reverse=False):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (not reverse and arr[j] < arr[i]) or (reverse and arr[j] > arr[i]):
                arr[i], arr[j] = arr[j], arr[i]

def main():
    arr = [-5, 6, 9, 3, 2, 0, 3, 87, 55]
    print(arr)
    bubble_sort(arr)
    print(arr)
    arr = [-5, 6, 9, 3, 2, 0, 3, 87, 55]
    print(arr)
    bubble_sort(arr, True)
    print(arr)


if __name__ == "__main__":
    main()