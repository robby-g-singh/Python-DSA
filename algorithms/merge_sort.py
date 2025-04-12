def merge_sort(lst):
    # recursive calls to keep dividing the list down until it reaches a length of 1:
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        # initialize variables to keep track of indices; i for left list; j for right list; k for merged list:
        i = 0
        j = 0
        k = 0

        # actual comparison operation:
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # check for any elements left over in the left list in the case of len(left) > len(right)
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        # check for any elements left over in the right list in the case of len(right) > len(left)
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


test = [8, 3, 500, 7, 12, 44, 23, 72, 0, 12, -91]
merge_sort(test)
print(test)
