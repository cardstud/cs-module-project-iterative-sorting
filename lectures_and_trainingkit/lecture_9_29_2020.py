"""LECTURE on ITERATIVE SORTING by Tom Tarpley (9-29-2020, 6:30pm-8:30pm)

AGENDA
======
1. Talk about Time Complexity
2. Linear Search
3. Binary Search
4. Linear vs Binary Search
5. Sorting Data
6. Looking at Insertion Sort
"""

""" TIME COMPLEXITY"""

animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Monkey']

# LINEAR TIME - O(n)
def print_animals(animal_list): # O(n)
    for i in range(len(animal_list)): # O(n) - looping over the dataset 
        print(animal_list[i])   # O(1) - print is not part of our code, animal_list[i] is O(1)
                                # for our purposes we ignore 'print'
                                # O(1) + O(k)  where k is the length of the string for our purposes we are ignoring

""" Getting the time complexity of an iterative solution
1. Compute the Big-O for each line in isolation
2. If something is in a loop, multiply it's Big-O by the loop for the total
3. If two things happen sequentially, add the Big-O
4. Drop Leading multiplicative constants from each Big-O
5. From all the Big-Os that are added, drop all but the biggest, dominating one
"""

""" Big-O Complexity Chart

From best to worse:
    1. O(1),            Excellent
    2. O(log  n)        Good
    3. O(n)             Fair
    4. O(n log n)       Bad
    5. O(n^2)           Horrible
    6. O(2^n)           Horrible
    7. O(n!)            Horrible
"""
# Let's figure out the time complexity of this code
def print_animals_a(animal_list):   # O(n) Linear
    for i in range(len(animals)):   # O(n)
        print(animal_list[i])       # O(1) * n so its (1*n)
        my_number = 0               # O(1) so (1*n)
        # O(2 * n)
        for _ in range(100000):     # O(100000) (100000 * n)
            my_number += 1          # O(1)  (1 * 100000) O(100000)

        # Drop leading multiplicative constants such as O(1000003*n) and O(100000*1)
            # O(100003 * n) => O(n)
            # O(100000 * 1) => O(1)

        # Keep just the biggest term
            # O(n)

# note: above is not O(n*n) because second loop has a constant:  range(100000). So its O(n)

# POLYNOMIAL TIME - O(n^c) where c is a constant
""" Key Points:
    1. This gets bad quickly, but a computer can normally handle an n of a few hundred
    2. It's easy to confuse this with exponential time. The difference here is that the number
            grows but the exponent stays the same
    3. The keywords for polynomial are pairs, triplets, etc. Sometimes you have to get this - find ...?
    4. One point of algorithms and data structures is to improve solutions that have this runtime or worse
"""
# Print a list of all possible animal pairs
def print_animal_pairs():   # O(n^2)
    for animal_1 in animals:    # O(n)
        for animal_2 in animals: # O(n)
            print(f"{animal_1} - {animal_2}")   # O(1)

# Print a list of all possible animal triples
def print_animal_triples():
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")

# Print a list of all possible animal triples
def print_animal_triples_a():
    # O(n)
    for animal in animals:
        print(animal)
    # O(n^3)
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")

# EXPONENTIAL TIME - O(c^n)  where c is a constant
"""KEY POINTS
1. This gets bad extremely quickly. Between 30 and 40, even simple processes break down
2. It's easy to confuse this with polynomial time. The difference is that here, the exponent grows, but the
        number stays the same
3. The keywords for exponential are 'all', 'combinations', 'groups', etc.
4. Combination locks have a bad name - they're really permuatation locks
"""

# Given a list,
# Return a List fo all possible combinations of animals
def get_animal_combos(l):
    list_length = len(l)
    if list_length == 0:
        return [[]]
    else:
        animal_combos = []
        previous_combos = get_animal_combos(l[1:])
        for combo in previous_combos:
            animal_combos.append(combo)
            animal_combos.append(combo + [l[0]])
        return animal_combos

# counter = 0
# def get_animal_combos(L):
#     global counter 
#     List_Length = Len(L)
#     if list_length == 0:
#         return [[]]
#     else:
#         animal_combos = []
#         previous_combos = get_animal_combos(L[1:])

#         for combo in previous_combos:
#             animal_combos.append(combo)
#             animal_combos.append(combo + [L[0]]
#         return animal_combos 
  
# print(get_animal_combos(animals))
# print(counter)



# FACTORIAL O(n!)
"""Key Points
1. Factorial time is the worse time complexity that we have dealt with on a normal basis
2. The keywords for exponential are 'all', 'permutations', 'orders', 'arrangments', etc.
3. Combination Locks have a bad name - they're really permutation lcoks!
"""

def get_all_arrangements(l):
    list_length = len(l)
    if list_length <= 1:
        return [l]
    else:
        arrangements = []
        previous_arrangments = get_all_arrangements(l[1:])
        for previous_arrangment in previous_arrangments:
            for i in range(len(previous_arrangment) + 1):
                arrangements.append(previous_arrangment[i:] + [l[0]] + previous_arrangment[:i])
        return arrangements

# LOGARITHMIC TIME
"""KEY POINTS
1. Look for division that dramatically reduces the remaining data for hints that this might be logarithmic
2. Often, this means dividing the data in each step
3. Key words are 'sorted list', 'binary', 'tree'
"""

# free all the animals, half at a time
# (remove them from the array)
def free_animals(animals):
    while len(animals) > 0:
        animals = animals[0:len(animals) //2 ]


""" LINEAR SEARCH

Key points:
-----------
1. Linear search is the simplest of search we can do
2. Sometimes it's the only method available. If the data is unordered, this is the only way to do it
3. It also beats a binary search under some special circumstances
4. Key words: unsorted, random

dataset [0 7 4 2 9 3 12]

    if we want to search for a 2 in this dataset using a linear search:
        Check 0, is that a 2 - no, ok move to next one
        Check 7, is that a 2 - no, ok move to next one
        Check 4, is that a 2 - no, ok move to next one
        Check 2, is that a 2 - yes, i found it, return the index or just say yes, there is a 2 there
    if we want to find a 12, need to go through the whole thing to find it, then ret index or say yes its there
    if we want to find a 42, we need to go through whole thing to find out its not in there
"""
# Code example
import random
import time 

my_range = 100
my_size = 100

print()
my_random = random.sample(range(my_range), my_size)
print(my_random, '\n')

searching_for = 7

# Linear search example
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True   # could return i
    return False 

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i 
#     return -1

my_arr = ([2, 6, 1, 25, 34, 29])
target = 34
print(linear_search(my_arr, target), '\n')


"""BINARY SEARCH

Key points:
1. Binary search requires sorted data
2. Each pass, we cut the remaining possibilities by half, hence the term binary
3. Key words: sorted, ordered
"""

def find_value_binary(arr, value):
    first = 0            # first index
    last = (len(arr)-1)  # last index
    found = False

    # could use for loop but will While loop
    # want to keep it in a positive numbers range

    while first <= last and not found:   # as soon as we get found true we jump out of this loop
        # find the middle of the data first
        middle = (first + last) // 2     # use floor division to make sure we get an integer, not a float

        if arr[middle] == value:
            found = True 
        
        else:
            # left case
            # search lower half
            if value < arr[middle]:
                last = middle - 1
            else:
                # right case
                # search uppper half
                first = middle + 1 

    return found 

""" Linear vs Binary search

Key Points:
----------
1. Binary search is only faster if the data is sorted
2. It's slower for the first search if the data needs to be sorted first
3. Subsequent searches will be much faster
4. Linear is good and simple
5. Binary more complex and requires sorted data
"""
print("Linear")
start = time.time()
print(linear_search(my_random, searching_for))
end = time.time()
print(f'Runtime: {end - start}', '\n')

print("Binary")
start = time.time()
my_random.sort()
print(find_value_binary(my_random, searching_for))
end = time.time()
print(f'Runtime: {end - start}', '\n')

# Let's see what happens with multiple runs

print("Linear Again")
start = time.time()
print(linear_search(my_random, searching_for))
end = time.time()
print(f'Runtime: {end - start}', '\n')

print("Binary")
start = time.time()
my_random.sort()
print(find_value_binary(my_random, searching_for))
end = time.time()
print(f'Runtime: {end - start}', '\n')

print("Binary _after_ sort")
start = time.time()
my_random.sort()
print(find_value_binary(my_random, searching_for))
end = time.time()
print(f'Runtime: {end - start}', '\n')

""" SORTING DATA

Lets say we have a python list of numbers that we want to sort: (sorting in general)

    my_list = [8,2,5,4,1,3]

We can start just by arbitrarily that the left side is sorted, and that the number there is already sorted.
We can do this by definition, one element_is_sorted. 
There are no other configurations to put the data in.

I'll mark this example by adding some space, but to the computer, there is still just a normal array

    my_list = [8,   2,5,4,1,3]

The next step is to look at the first element in the unsorted side and determine where it goes.
If it's greater than that, it stays in the same place. If not, we move it left 1 box.

If it's larger, or it's now the first index, we've found it's home. 
Otherwise, we continue with the same process

2 is less than 8, so we pop the 2 out to a temp variable, move the 8 to the right.

    my_list = [8,   2,5,4,1,3]
    my_list = [8,   8,5,4,1,3]

Then we determine if the two goes in the 8's old spot.
What are the two rules? If it's bigger or at the first element. 
So the 2 is now up front and the first two elements are sorted

    my_list = [2,8  5,4,1,3]

We continue the process with the 5, its less than 8 but greater than 2

    my_list = [2,5,8    4,1,3]

From here, we go element by element, until all the elements are on the sorted side

INSERTION SORT
==============

Key points:
----------
1. A problem with a defined start and end point lends itself to an iterative solution
2. Management of iteration is key to solving this problem

"""

l = [8,2,5,4,1,3]
# tmp_var = l[1]  # ==> 2
print(l, '\n')

# Implement an insertion sort algorithm
def insertion_sort(list_to_sort):
    # separate the first element and think of it as sorted
    # Let us say it's the first item in the list

    # for all other items (on the right of the first index) we want to loop
    # range based starting at index 1
    for i in range(1, len(list_to_sort)):
        # put the current number into a temporary variable
        temp = list_to_sort[i]  # grabs 2 first

        # keep track of our current index as j (decrement it) j is in our while loop
        curr_index = i

        # keep Looking left until we find our temp number belongs
        # while curr_index > 0 (we are not past the start of the indices) and our temp
        #   and our temp variable is < the number to the left of curr_index
        while curr_index > 0 and temp < list_to_sort[curr_index-1]:
         # as we look left, shift the items to the right as we iterate
            list_to_sort[curr_index] = list_to_sort[curr_index-1]
            # decrement curr_index
            curr_index -= 1
        # when left is smaller than our temp variable, or we are at zero, put the item at that spot
        list_to_sort[curr_index] = temp 
    # return list back to caller
    return list_to_sort 

# Lets try it
insertion_sort(l)
print(l)