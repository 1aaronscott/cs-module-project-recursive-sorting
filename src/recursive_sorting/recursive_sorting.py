# TO-DO: complete the helper function below to merge 2 sorted arrays
from math import floor


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
#    merged_arr = [0] * elements

    # Your code here
    # compare first elements of arrA and arrB
    # remove the smaller from arrA or arrB and put into merged_arr
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] >= arrB[0]:
            merged_arr.append(arrB.pop(0))
#            print(merged_arr)
        else:
            merged_arr.append(arrA.pop(0))
#            print(merged_arr)

    # handle any leftover list elements
    while len(arrA) > 0:
        merged_arr.append(arrA.pop(0))
    while len(arrB) > 0:
        merged_arr.append(arrB.pop(0))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # deal with lists of one or zero values
    if len(arr) <= 1:
        return arr

    # split the input list into two roughly equal lists
    midpoint = floor(len(arr)/2)
    left = arr[:midpoint]
    right = arr[midpoint:]
    # print(left, right)

    # recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # join and return final sorted lists
    arr = merge(left, right)
    return arr


#print(merge_sort([1, 4, 6, 7, 0, 5, 2, 3, 9, 8]))

# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
