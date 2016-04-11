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

    for item in my_list:
        print item


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """

    odd_list = []
    for num in number_list:
        if num % 2 != 0:
            odd_list.append(num)

    return odd_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    even_list = []
    for num in number_list:
        if num % 2 == 0:
            even_list.append(num)

    return even_list


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """

    every_other = []
    for item in my_list[::2]:
        every_other.append(item)
    
    return every_other


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

    for i in range(len(my_list)):
        print "{} {}".format(i, my_list[i])


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    long_words = []
    for word in word_list:
        if len(word) > 4:
            long_words.append(word)

    return long_words


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """

    n_words = []
    for word in word_list:
        if len(word) > n:
            n_words.append(word)

    return n_words


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

    find_int = sorted(number_list)
    if len(find_int) > 0:
        return find_int[0]
    else:
        return None


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

    find_int = sorted(number_list)
    if len(find_int) > 0:
        return find_int[-1]
    else:
        return None


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    halvesies_list = []
    for num in number_list:
        halvesies_list.append(float(num)/2)
    
    return halvesies_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    length_list = []
    for word in word_list:
        length_list.append(len(word))

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

    sum = 0
    for num in number_list:
        sum = sum + num
    
    return sum


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

    mult = 1
    for num in number_list:
        mult = mult * num
    
    return mult


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

    if len(word_list) > 0:
        new_string = ""
        for word in word_list:
            new_string = new_string + word
        return new_string
    else:
        return ""


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    list_total = 0
    for num in number_list:
        list_total = float(list_total) + float(num)
    list_nums = len(number_list)
    if list_nums == 0:
        pass
    else:
        return list_total / list_nums


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    if len(list_of_words) > 1:
        word_list = ''
        for word in list_of_words:
            word_list = word_list + word + ', '
        return word_list.rstrip().rstrip(',')
    else:
        return list_of_words[0]


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
    
    return set(foods1) & set(foods2)


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """

    return my_list[::-1]


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions 
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list_in_place([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list_in_place(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """

    my_list.reverse()
    return my_list


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list. 
       The returned list should be in ascending order.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]

    """

    singles = set(my_list)
    uniques = []

    for item in my_list:
        if item in singles:
            singles.remove(item)
        else:
            uniques.append(item)

    uniques = set(uniques)
    return list(uniques)


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

    return []


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a 
    list of the largest n numbers in the input list in ascending order. 

    You can assume that n will be less than the length of the list. 

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """

    input_list.sort()
    input_list.reverse()
    # print input_list
    ######[6006, 700, 59, 42, 6, 2]

    largest_nums = []
    for i in range(len(input_list)):
        if i < n:
            largest_nums.append(input_list[i])
    
    largest_nums = set(largest_nums)
    return list(largest_nums)
    

##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
