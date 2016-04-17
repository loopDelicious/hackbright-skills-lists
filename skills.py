"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
# For every iterable item in the list, print the element

    for element in my_list:
        print element


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    odds_list = []  # Create an empty list
    
    for element in number_list:  
        if element % 2 != 0:  # If the element is not divisible by 2, or odd
            odds_list.append(element)  # Append the element to odds_list

    return odds_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    evens_list = []

    for element in number_list:
        if element % 2 == 0:    # If the element is divisible by 2, or even
            evens_list.append(element)

    return evens_list 


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    # Create a new list that includes the original list, moving by steps of 2
    
    every_other_list = my_list[::2]
    
    return every_other_list


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    # Use enumerate function to iterate and print index and element

    for index, element in enumerate(my_list):
        print index, element


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    new_list = []

    for word in word_list:
        if len(word) > 4:  # If the length of the word is longer than 4 characters
            new_list.append(word)  # Add the word to the new list

    return new_list


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """

    new_list = []

    for word in word_list:
        if len(word) > n:  # If the length of the word is longer than n characters
            new_list.append(word)  # Add the word to the new list

    return new_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    if len(number_list) == 0:  # If input list is empty, return None
        return None

    smallest = number_list[0] # Bind the variable smallest to the value of the first element

    for number in number_list:
       if number < smallest:  # If any element is smaller than the smallest,
            smallest = number  # bind the new value that is smallest to variable smallest
     
    return smallest         


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    if len(number_list) == 0: # If input list is empty, return None
        return None

    largest = number_list[0]  # Bind the variable largest to the value of the first element

    for number in number_list:
        if number > largest:  # If any element is larger than the largest,
            largest = number  # bind the new value that is larger to variable largest

    return largest


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    half_list = []

    for number in number_list:
        half_list.append(float(number)/2)  # Divide each element by 2, format as float
    
    return half_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    length_list = []

    for word in word_list:
        length_list.append(len(word))  # use len function to determine length of string

    return length_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    total = 0  # Set variable total to zero

    for number in number_list:  
        total += number   # Add each element to the total cumulatively

    return total


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    if len(number_list) == 0:  # Product of an empty list will be 1
        return 1
    
    total = 1  # Set variable total to 1

    for number in number_list:  
        total *= number   # Multiply each element to the total cumulatively

    return total


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    my_string = ""  # Create an empty string

    for word in word_list:
        my_string = my_string + word # Concatenate each word upon each iteration

    return my_string


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    total = 0

    for number in number_list:
        total += number  # Sum the numbers in the list
    
    return float(total)/len(number_list)  # Return total formatted as float by number of elements in the list


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    my_string = ", ".join(list_of_words) # Use join function to join words with comma

    return my_string


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods, 
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)
    
    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """

    return set(foods1) & set(foods2)  # Return the intersection of 2 sets


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """

    return my_list[::-1]  # Return the full list moving backwards by step -1



def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions 
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """

    return my_list[::-1]  # Return the full list moving backwards by step -1


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]
    

    """
    dupes = set()  # Created an empty set, which naturally de-dupes

    for item in my_list:
        if my_list.count(item) > 1:  # If there's more than 1 occurrence
            dupes.add(item)  # Add item to the set
 
    dupes_list = list(set(dupes))  # Convert set to list data structure, so it can be ordered
    dupes_list.sort()  # Sort in ascending order
    return dupes_list

def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """

    results = []
    for index, word in enumerate(list_of_words):  # Use enumerate to access indices
        if letter in word:
            results.append(index)
        else:
            results.append(None)

    return results


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a 
    list of the largest n numbers in the input list in ascending order. 

    You can assume that n will be less than the length of the list. 

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    largest_list = []

    while n > 0:    # Do the loop for n number of times
        largest_list.append(max(input_list))  # Add the maximum value to the largest_list list
        input_list.remove(max(input_list))  # Remove the maximum value from the original list
        n -= 1  # Decrement the number of times to repeat the loop

    largest_list.sort()  # Sort in ascending order

    return largest_list
    # while n > 0:
        
    #     for number in input_list:
    #         largest_number = input_list[0]
    #         if number > largest_number:
    #             largest_number = number
    #         largest_list.append(largest_number)
    #     del largest_number
    #     n -= 1

    # return largest_list

    # largest_list = []
    # new_list = input_list.sort()
    
    
    # while n > 0:
    #     largest_number = new_list[-1]
    #     largest_list.append(largest_number)
    #     del new_list[-1]
    #     n -= 1

    # return largest_list


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
