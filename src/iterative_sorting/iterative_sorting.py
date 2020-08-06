# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        smallest_value = arr[cur_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for unsorted_index in range(cur_index, len(arr)):
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

# test it
arr=[5, 55, 6, 67, 16, 9, 25, 43, 12, 2, 7, 88, 45, 6]
print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # pass through the array and peform no swaps
    swaps_occurred = True
    # iterating through the arr and looking at elements two at a time
    #    and swapping them if they're out of order
    while swaps_occurred:
        # toggle swaps_occurred boolean to False at beginning of while loop 
        swaps_occurred = False
    # if we do this all the way through, all the elements will
    #    eventually end up in sorted order
        for i in range(len(arr) - 1):    # i is the left element of the two values we are looking at
            # we need to swap if arr[i] > arr[i+1]
            if arr[i] > arr[i+1]:
                # swap them
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True 
    
    return arr 

# Test it
#arr = [13, 15, 6, 18, 3, 27, 19, 22]
arr = [5,1,7,6,2,1,0]
bubble_sort(arr)  # dont print this, we let it finish then print below
print(arr)


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# def counting_sort(arr, maximum=None):
#     # Your code here


#     return arr
