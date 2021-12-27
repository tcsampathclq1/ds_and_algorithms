def binary_search(arr, low, high, elem):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if elem == arr[mid]:
        return mid
    elif elem < arr[mid]:
        return binary_search(arr, low, mid-1, elem)
    else:
        return binary_search(arr, mid+1, high, elem)


def main():
    arr = [1,3,5,7,9,11,13,15]
    res = binary_search(arr, 0, len(arr)-1, 13)
    print("index is " + str(res))

if __name__ == "__main__":
    main()