""" ITERATIVE SORTING MOUDLUE

PRECLASS TRAINING KIT

Algorithm: a set of instructions for accomplishing a task
    We want the most efficient algorithm (considering both 'time' and 'space' efficiency)

BIG O NOTATION:
==============
Big O is a way of describing the rate of change in the execution speed when the data size increases. It how we describe how long an algorithm runs and 
    it is a way to compare different algorithms efficiencies.

    The specific terms of Big O notation describe how fast the runtime grows (relative to the size of the input) with a focus on when the input gets very large.

Different computers have different runtimes so by focusing on the general growth, we can avoid the differences in exact runtime betweeen machines and environments.
We also talk about runtime relative to the input size because we need to express our speed in terms of something so we show the speed of the algorithm in terms of
    the input size. This allows us to see how the speed reacts as the input size grows. (we dont care about speed when input size is small)

COMMON BIG O RUN TIMES:
======================

Classification           What it means                                                                                                                
--------------           -------------                                                                                                            
Constant O(1)           The runtime or space used is completely unaffected by the size of the input; the ideal solution  
Logarithmic O(log n)    As the size of the input increases, the runtime or space used will grow at a slightly slower rate; pretty good solution
Linear O(n)             As the size of the input increases, the runtime or space used will grow at the 'same' rate; generally acceptable solution
Linearithmic O(n log n) As the size of the input increases, the runtime or space used will grow at a slightly faster rate; usable but might not be an ideal solution
Polynomial O(n^c)       As the size of the input increases, the runtime or space used will grow at a faster rate; solutin may work for handful of small inputs but is in no way scalable
Exponential O(c^n)      As the size of the input increases, the runtime or space used will grow at a much faster rate; a pretty inefficient solution
Factorial O(n!)         As the size of the input increases, the runtime or space used will grows at astronomically, even with relatively small inputs; extremely slow solution
"""
import timeit
import numpy as np
import math 

# Some examples
items = [1, 5,'A', 22, 'b', 'tom', 8]
# items = np.arange(250)

# CONSTANT TIME O(1)
#   The below is constant time because no matter how large or small the input is, the number of computations within the function is the same.
def print_one_item(items):
    print(items[0])

start = timeit.timeit()
print(print_one_item(items))
end = timeit.timeit() 
print('The time to run this is: ', round(end-start,7), 'seconds.')
ct = round(end-start,7)

# LINEAR TIME O(n)
#   This is linear time because the speed of the algo increases at the same rate as the input size.
#       if 'items' has ten items, then the function will print 10 times; if it has 10,000 items, it will
#           print 10,000 times.
def print_every_item(items):
    for item in items:
        print(item)

start=timeit.timeit() 
print(print_every_item(items), '\n')
end = timeit.timeit() 
print('The time to run this is: ', round(end-start,7), 'seconds.')
lt = round(end-start,7)

# QUADRATIC TIME O(n^2)
# This is quadratic time because the nested loops(clue that this is quadratic) mean that for each item in items(the outer loop),
#   we iterate through every item in items(the inner loop).
# For an input size of 'n', we have to print n*n times or n^2.
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

start=timeit.timeit()
print(print_pairs(items), '\n')
end = timeit.timeit() 
print('The time to run this is: ', round(end-start,7), 'seconds.', '\n')
qt = round(end-start,7)

print(f'Constant time example: {ct} seconds.\nLinear time example: {lt} seconds.\nQuadratic time example: {qt} seconds.')

""" WHAT ABOUT CONSTANTS"""

def do_a_bunch_of_stuff(items):
    last_idx = len(items)-1
    print(items[last_idx])

    middle_idx = len(items)/2
    idx=0 
    while idex<middle_idx:
        print(items[idx])
        idx=idx+1

    for num in range(2000):
        print(num)

"""
print(items[last_idx]) is constant time because it doesn't change as the input changes. That portion of the function  is:           O(1)
The while oop that prints up to the middle index is 1/2 of whatever the input size is, we can say that portion of the function is:  O(n/2)
The final portion will run 2000 times, no matter the size of the input.

So putting it all together, we say the efficiency is:   O(1 + n/2 + 2000). - We dont say this though, we just describe the function as having
    linear time O(n) because we drop all of the constants.
We drop the constants because as the input size gets huge, adding 2000 or dividing by 2 has minimal effect on the performance of the algorithm

MOST SIGNIFICANT TERM
---------------------"""

def do_different_things(items):
    for item in items:
        print(item)

    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

"""This function could be described as O(n + n^2); however, we only need to keep the essential term, which is n^2, so this is: O(n^2)
    We can do this because as the input size, n, gets larger, the less significant terms have less of an effect, and only the most significant term matters.


BIG O represents the worst-case"""

def search_for_thing(items, thing):
    for item in items:
        if item == thing:
            return True
    return False 

"""If the 'thing' we are looking for in items is very first item then it would be O(1)
   If it were the last 'thing' in items then it would be O(n).

So when we talk about the complexity of a function, we usually assume the "worst case", which is if the 'thing' was last in this case, O(n)

Note: 
    Big theta gives both an upper and lower bound for the running time.
    Big O only gives an upperbound

DO constants ever matter?

Just because two algos have the same Big O notation doesnt mean they are equal

Example: suppose you have a script that takes 1 hour to run. 
         -By improving the function,you can divide that runtime by six and now it only takes 10 minutes to run.
         -With Big O notation, O(n) and O(n/6) can both be written O(n) but that doesn't mean it isn't worth optimizing the script to save 50 minutes
            every time the script runs.

premature optimization(xkcd: Optimization (xkcd.com/1691/)
    Sometimes you can sacrifice readability or spend too much time on something to improve its efficiency
    Depending on the situation, it could be that having a finished product to iterate on is more important than maximally efficient code.
    You will always be making calculated tradeoffs between runtime, memory, development time, readability and maintainability.
"""

# Code snippets to exhibit some runtime classifications

# we can use the process of elimination to narrow down which runtime classification makes sense for this algorithm
# The number of times the loop runs seems to vary based on the value of 'n', so this is NOT O(1)
# We can also see that the number of times the loop runs is increasing slower than the size of the input is increasing.
#   n must be doubled before the loop will ru n one more time so we can eliminate O(n log n), O(n^c), O(c^n), and O(n!)
# The only two otions left are logarithmic or linear.
#   Since the two rates of growth(input, the number of operations) are not the same, this function must run in logarithmic time.

def foo(n):
    i = 1 
    while i < n:
        print(i)
        i *= 2

print(foo(100), '\n')
print(foo(10), '\n')


"""CHALLENGE

1. Classify the runtimes of each of the following scenarios:

A. You are searching for a specific name in a phone book(that is sorted alphabetically). ---- O(n) because worst case you have to go through whole list
B. You meet someone, and they give you their phone number. You realize later you forgot their name. To match their name, you look through 
        a phone book until you find their phone number. --------O(n) because worst case you have to go through whole phone book

2. Classify the runtimes of each of the following functions:
"""
# linear time - O(n)
def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)

foo(4)

# quadratic time - O(n^2)
def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, x):
            for k in range(x, x+15):
                sum += 1
print() 
print()
""" LINEAR SEARCH

Going through the list one by one
Examples: Guessing a number 1 - 1000 and only choices are right or wrong
          Collecting ticket stubs and then seeing if the person that purchased F16 showed up
"""

"""BINARY SEARCH
On average, its best to take the middle or average (example: guessing a number 1-1000)
    You start at 500 and ask if too high or too low - then repeat each time halving it

LOGARITHMS:
----------
The situation where you are halving the number of possibilities each time, mathematically, is considered a logarithm

Logs:  10^2 = 100 means 10 multiplied by itself 2 times equals 100
       log10(100) = 2 is the inverse of above, means how many 10s would we have to multiply to equal 100, the answer is 2
    
Halving numbers each time, like in Binary search, is log2(n), just like if we doubled numbers each time, it's n^2.
Whenver we talk about logarithms in relation to describing the runtime of an algorithm, we are talking about log2(n)

When we talk about logarithms in computing, we almost always mean log2() because computers operate on binary or a base 2 number system.

FOLLOW ALONG:
------------
"""
# write a binary search function; expect a 'sorted' list of integers; return position of integer in list we are searching for if it exists
# 1. Need to set two different pointers: low(1st item in list) and high(last item in list)
# 2. Set up a loop that will continue while the 'low' pointer is less than or equal to the 'high' pointer. 
# 3. Next we need to do get the middle index: do that by averageing 'low' pointer and 'high' pointer(rounding down) 
#       We do that by adding the 'low' pointer to the 'high' pointer and divide by 2(using floor division //)
# 4. Now use middle index to retrieve the item with that index from our list
# 5. Now that we have the guess, there are three options
#       a. our guess is correct
#       b. our guess is too high
#       c. our guess it too low
# 6. With logic set, write what happens with each option. 
#       a. if guess is equal to search_item then middle index is correct and return the index
#       b. if guess is too high(greater than our search_item), then change 'high' pointer to the index directly below the current 'middle' value
#       c. if guess is too low(lesser than our search_item), then change 'low' pointer to the index directly above the current 'middle' value
# 7. If search_item is not in my_list then terminate the loop without returning from the function which should return the None value
def binary_search(my_list, search_item):
    low = 0
    high = len(my_list)-1

    while low <= high:
        middle = (high+low) // 2 
        guess = my_list[middle]

        if guess ==search_item:
            return middle 
        if guess > search_item:
            high = middle - 1 
        else:
            low = middle + 1  
    return None 

# test it
test_list = [2,4,7,8,9,10,12,34,45]

print(binary_search(test_list, 7))
print(binary_search(test_list, 39),'\n')

"""CHALLENGE
1. Suppose your app has 16,384 users that are stored in a database(users are stored alphabetically). Your app need to search for a specific userand you use binary search.
     What's the maximum number of steps it would take? (Hint: using the logarithmic operation is key)

2. Time passes and now your app has 'exactly double' the number of users. 
     What's the maximum number of steps now?

3. Try writing a Python function to perform a linear search on a set of data
4. Try writing your own Python function to perform a binary search on a set of data. This will help you remember and internalize this algorithm much better if you do not refer
     refer to our example above. Make sure to use UPER as you approach this
5. Can you rewrite your binary search function so it uses recursion?
"""

""" SELECTION SORT 
    ==============

Sorting helps make searching and finding a specific item easier. 

out-of-place selection sort:
---------------------------
Book example:
    We want to sort books on a shelf alphabetically by title starting on the left
    Most natural way would be to scan the books from left to right, looking for book title with lowest alphabetical title
    We find "Animal Farm" and take that book and place it all the way to the left
    Now we go through the books again, looking for the next book with the lowest alphabetical title
    We repeat this until the books are all sorted

    This worked because we had a lot of room on our shelf but what if there is no extra room? Then we need to sort the books in-place.
    That means instead of creating a new collection of books we need to swap books as we encounter them.


In-place selection sort:
-----------------------
Book example again:
    Start by looking through each book from left to right, keeping track of the lowest book we find.
    Once we find it, "Animal Farm", we swap the lowest book with the first position.
    We repeat this whole process but we start at the second position and will swap the lowest book with the second position when we find it
    During this loop, the book in second position is already "lowest" book so no swapping takes place
    We repeat this process now starting at the third position.
    Each time we loop through we increment our starting position by 1 until we get to the last position in the collection
"""

""" INSERTION SORT
    ==============

Insertion sort is an efficient algorithm for sorting 'small amounts' of data

PLaying cards example:
    When you sort cards, you start with an empty left hand then take one card at a time from a pile of cards that is face down on the table.
    With each card you pick up, you insert it into the correct position in the left hand
    To do so, you compare the current card to each card already in the left hand, starting at the rightmost card.
    If the current card is smaller, you swap positions
    You keep doing this while the current card is smaller than the card on the left
    Once the current card is not smaller than card on the left, you can stop and pick up a new card

Complexity analysis:
    Insertion sort runs in O(n) time  in it's best case
                   runs in O(n^2) time in its worst and average cases

    If the colletion is already sorted, the insertion sort algorithm will still have to go through each item in the collection to make sure
        its in the right spot.
    The worst case would be if the collection was sorted in descending order. This would require us to do the maximum number of iterations to
        shift items to the right and will be O(n^2)
    For the average case, the number of inner loops will not be the maximum but since constants do not matter, it will still be O(n^2)
"""

"""BUBBLE SORT
   ===========

Bubble sort is one of the simplest but very inefficient algorithms.

Described by:
    1. Compare the first and second item of a collection. If the first item is bigger than the second item, swap the items
    2. Move to the next item. Compare the 2nd item with the 3rd item, if 2nd is bigger then swap them
    3. Do this for every item until the end of the list
    4. Repeat steps 1-3(decrementing "the end of the list" by 1 each time)

Complexity Analysis:
    Even if the list is already sorted, we still have to touch every item in the list. 
    That means the best case has an O(n) runtime complexity (where only the outer loop runs)
    In the worst case, the inner loop has to perform 1/2 * n operations due to swapping every element
    Remembering we drop constants in the Big O notiation, this means that the entire algorithm's complexity (inner and outer loop) can 
        be represented in Big O with O(n*n) or O(n^2)
"""

"""CODE for SELECTION SORT"""

#  a collection of integers that are unsorted and we need to sort them (using an 'in-place' selection sort)
our_numbers = [5,9,3,6,2,1,7,8,4]

# define selection_sort function

# we start by setting up our outer loop with 'for i in range(0, len(items)-1): this is the loop that says 
#   we will go through each item in our collection, one at a time.
# Next we define what to do for each item in the collection - need to loop through all the items that come
#   after the current index to find the one with the lowest value
# We do this with another loop. With each item, we check if it is smaller than the current smallest and replace
#   the smallest index if so
# At the end, before we increment our outer loop, we swap the item that is located in the current index with
#   the smallest item that we located during our loop
def selection_sort(items):
    # Outer loop
    for i in range(0, len(items)-1):
        cur_index = i 
        smallest_index = cur_index 
        for j in range(cur_index + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j
        
        items[smallest_index], items[cur_index] = items[cur_index], items[smallest_index]

    return items 

# test it
print(selection_sort(our_numbers), '\n')

"""Runtime Complexity

The Big O for the outer loop is O(n) since we are going through each item in our data
Each time our outer loop increments, our inner loop decreases by 1. On average, we check a list of 1/2 x n
This means the runtime for the algorithm could be represented as O(n x 1/2 x n) but since in Big O we can
    often ignore the constants, then the true Big O is O(n x n) which is O(n^2)

Challenge:
---------
1. What will the contents of the array that is shown below look like after each pass of the SELECTION SORT algorithm?

25  67  4   33  19  40
4   67  25  33  19  40
4   19  25  33  67  40
4   19  25  33  67  40
4   19  25  33  40  67

2. Define your own function that sorts the data "out-of-place" and mirrors the process we used for our "out-of-place" book sorting example.
     Compare this "out-of-place" selection sort to the "in-place" function that we defined together.
     What is different about it?
     Which veresion do you think is better and why?

3. What will the contents of the same array look like after each pass of the INSERTION SORT algorithm?
---ask Tom T about this to check this
25  67  4   33  19  40
25  67  4   19  33  40
4   25  67  19  33  40?

4. You have the cards 2,7,3,4 and 6. Write and algorithm in pseudo-code that arranges the cards in ascending order

5. What will the contents of the array below look like after each pass in the Bubble Sort algorithm?

25  67  4   33  19  40
25  4   33  19  40  67
4   25  19  33  40  67
4   19  25  33  40  67

6. What would the following array look like after one iteration of Bubble Sort?

    my_arr = [3,6,4,12,11,15,1,2]

3   4   6   11  12  15  1   2
=========================================================================================================
========================================================================================================="""
