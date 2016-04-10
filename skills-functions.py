# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def write_hello_world():
    """print 'Hello World' """

    print "Hello World"

write_hello_world()

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def greeting(name):
    """print greeting"""

    print "Hi", name

greeting("Christina")

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def multiply(num1, num2):
    """multiply two integers together"""
    
    return int(num1) * int(num2)

print multiply(4, 6)

# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def str_repeater(string_arg, num):
    """repeat a string value"""

    print str(string_arg) * int(num)

str_repeater("spaghetti", 8)

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def zero_finder(num):
    """evaluate integer in relation to zero"""

    if int(num) == 0:
        print "Zero"
    elif int(num) > 0:
        print "Higher than 0"
    else:
        print "Lower than 0"

zero_finder(565)

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divis_by_three(num):
    """determine whether integer is divisible by 3"""

    return int(num) % 3 == 0

print divis_by_three(7)

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def find_spaces(string_arg):
    """count the number of spaces in a sentence"""

    return string_arg.count(" ")

print find_spaces("The rain in Spain stays mainly in the plain")


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def tip_calculator(meal_price, tip=15):
    """calculates total bill for a meal, inclusive of tip. If no tip percentage is provided, 
    calculate tip based on 15 percent of the bill"""
   
    total_bill = meal_price + meal_price * (tip/100)
    return "${:.2f}".format(total_bill)

print tip_calculator(float(34), float(20))


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


def num_evaluator(num):
    """evaluate an integer's sign (positive or negative) and parity (even or odd); return a list"""
    evaluation = []
    if num == 0:
        pass
    else:
        if int(num) > 0:
            evaluation.append("Positive")
        elif int(num) < 0:
            evaluation.append("Negative")
    if int(num) % 2 == 0:
        evaluation.append("Even")
    else:
        evaluation.append("Odd")
    return evaluation

print num_evaluator(55)

sign = num_evaluator(-63)[0]
parity = num_evaluator(44)[1]
print sign
print parity


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
