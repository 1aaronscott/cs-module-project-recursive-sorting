# TO-DO: complete the helper function below to merge 2 sorted arrays
#import random
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
            print(merged_arr)
        else:
            merged_arr.append(arrA.pop(0))
            print(merged_arr)

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
#print(merge_sort(random.sample(range(200), 50)))

# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # Your code here

    # Maintain two pointers which point to start of the segments which have to be merged.
    # Compare the elements at which the pointers are present.
    # If element1 < element2 then element1 is at right position, simply increase pointer1.
    # Else place element2 in its right position and all the elements at the right of element2 will be shifted right by one position. Increment all the pointers by 1.
    pointer1 = start+1
    if arr[start] <= arr[pointer1]:
        return arr

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) <= 1:
        return arr

    midpoint = floor((r-l)/2)
    merge_sort_in_place(arr, l, midpoint)
    merge_sort_in_place(arr, midpoint, r)

    merge_in_place(arr, l, midpoint, r)
    return arr

##### Begin: Merge in place code from instructor/geeksforgeeks.org: #######################


def merge_in_place(arr, start, mid, end):
    # start2 is the first element in the right
    # half of the list
    start2 = mid + 1

    # If the two halves we're merging are already
    # sorted, no need to do anything
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

        # we don't return anything in in-place functions
        # since we're directly mutating the input array


def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
##### End: Merge in place code from instructor/geeksforgeeks.org: #######################

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):
    # Your code here

    return arr
