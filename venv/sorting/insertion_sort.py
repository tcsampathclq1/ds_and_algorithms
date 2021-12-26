def insertion_sort(arr, reverse=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and ((not reverse and arr[j] > key) or (reverse and arr[j] < key)):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def main():
    arr = [-5, 6, 9, 3, 2, 0, 3, 87, 55]
    print(arr)
    insertion_sort(arr)
    print(arr)
    arr = [-5, 6, 9, 3, 2, 0, 3, 87, 55]
    print(arr)
    insertion_sort(arr, True)
    print(arr)


if __name__ == "__main__":
    main()