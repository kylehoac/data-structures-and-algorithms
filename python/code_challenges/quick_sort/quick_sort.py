def quick_sort(lst, left, right):
    if left < right:
        position = partition(lst, left, right)
        quick_sort(lst, left, position - 1)
        quick_sort(lst, position + 1, right)
    return lst

def partition(lst, left, right):
    pivot = lst[right]
    low = left - 1
    for i in range(left,right):
        if lst[i] <= pivot:
            low += 1
            swap(lst, i, low)
    swap(lst, right, low + 1)
    return low + 1

def swap(lst, i, low):
    temp = lst[i]
    lst[i] = lst[low]
    lst[low] = temp

# ALGORITHM QuickSort(arr, left, right)
#     if left < right
#         // Partition the array by setting the position of the pivot value
#         DEFINE position <-- Partition(arr, left, right)
#         // Sort the left
#         QuickSort(arr, left, position - 1)
#         // Sort the right
#         QuickSort(arr, position + 1, right)

# ALGORITHM Partition(arr, left, right)
#     // set a pivot value as a point of reference
#     DEFINE pivot <-- arr[right]
#     // create a variable to track the largest index of numbers lower than the defined pivot
#     DEFINE low <-- left - 1
#     for i <- left to right do
#         if arr[i] <= pivot
#             low++
#             Swap(arr, i, low)

#      // place the value of the pivot location in the middle.
#      // all numbers smaller than the pivot are on the left, larger on the right.
#      Swap(arr, right, low + 1)
#     // return the pivot index point
#      return low + 1

# ALGORITHM Swap(arr, i, low)
#     DEFINE temp;
#     temp <-- arr[i]
#     arr[i] <-- arr[low]
#     arr[low] <-- temp
