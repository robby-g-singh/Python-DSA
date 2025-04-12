def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def binary_search_recursive(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search_recursive(arr, target, mid + 1, end)
    else:
        return binary_search_recursive(arr, target, start, mid - 1)
