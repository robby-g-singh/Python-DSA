def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(): return


test = [1, 3, 5, 7, 9, 11, 13]
print(binary_search_iterative(test, 5))
