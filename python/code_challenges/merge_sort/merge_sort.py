def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    if n > 1:
      mid = n // 2
      left = lst[0:mid]
      right = lst[mid:n]
      merge_sort(left)
      merge_sort(right)
      return merge(left, right, lst)

def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1
        k = k + 1

    if i == len(left):
        lst[k:] = right[j:]
    else:
        lst[k:] = left[i:]
    return lst
