def merge_sorted_arrays(arr_1, arr_2):
    arr_3 = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            arr_3.append(arr_1[i])
            i += 1
        else:
            arr_3.append(arr_2[j])
            j += 1
    arr_3.extend(arr_1[i:])
    arr_3.extend(arr_2[j:])
    return arr_3

def main():
    arr_1= [1, 3, 5, 7, 9, 10, 11, 18]
    arr_2 = [2, 4, 6, 8, 10, 11, 18, 23, 89]
    arr_3 = merge_sorted_arrays(arr_1, arr_2)
    print(arr_1)
    print(arr_2)
    print(arr_3)

if __name__ == "__main__":
    main()