from functools import reduce
# Wave 1
# Write a function that takes in a list of words and returns the shortest
# one. (assume no ties)

def shortest_word(words):
    return min(words, key=len)

# SUPER CHALLENGE: use functools.reduce
# Only try this after completing the rest of the activity
# You will need to research the use of the functools.reduce function
# Wave 1
# Write a function that takes in a list of words and returns the shortest
# one. (assume no ties)

    
# SUPER CHALLENGE: use functools.reduce
# Only try this after completing the rest of the activity
# You will need to research the use of the functools.reduce function

def shortest_word(words):
    return reduce(lambda a, b: a if len(a) < len(b) else b, words)



# Wave 2
# Write a function that takes in a list of numbers and returns a new list
# containing only the ones that are even, in the same order.
# Hint: remember to convert back to a list!

def even_nums(nums):

    new_even_list = list(filter(lambda x: x % 2 == 0, nums))
  
            
    return new_even_list
    

# Wave 3
# Write a function that takes in a list of numbers and returns a new list
# containing the squares of those numbers (the numbers raised to the second power)
# Hint: remember to convert back to a list!

def squares(nums):
    new_squares_list = list(map(lambda x: x ** 2, nums))
    return new_squares_list
    

# Wave 4
# Write a function that accepts a word, a function, and the name of that 
# function. It should return a string that reports:
# "The result of applying FUNCTION_NAME to WORD is RESULT"

def report(word, function, function_name):
    result = function(word)
    return f"The result of applying {function_name} to {word} is {result} "

# Wave 5
# Write a function that takes a list of passwords and returns a list of only 
# those passwords that have at least one non-alphabetic character in them. 
# The returned list should be sorted by in order of increasing length.

def sorted_valid_passwords(passwords):
    new_passwords = []
    
    for pw in passwords:
        if not pw.isalpha():
            new_passwords.append(pw)
            
    return sorted(new_passwords, key=len)




# Wave 2
# Write a function that takes in a list of numbers and returns a new list
# containing only the ones that are even, in the same order.
# Hint: remember to convert back to a list!

def even_nums(nums):
    pass

# Wave 3
# Write a function that takes in a list of numbers and returns a new list
# containing the squares of those numbers (the numbers raised to the second power)
# Hint: remember to convert back to a list!

def squares(nums):
    pass

# Wave 4
# Write a function that accepts a word, a function, and the name of that 
# function. It should return a string that reports:
# "The result of applying FUNCTION_NAME to WORD is RESULT"

def report(word, function, function_name):
    pass

# Wave 5
# Write a function that takes a list of passwords and returns a list of only 
# those passwords that have at least one non-alphabetic character in them. 
# The returned list should be sorted by in order of increasing length.

def sorted_valid_passwords(passwords):
    pass

