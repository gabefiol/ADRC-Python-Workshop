# Python Workshop 1

# First we'll import (download, add, etc.) some modules
# Modules - These are like toolboxes, they contain a set of tools (functions) that help us do more things (quicker)
    # ex. numpy has a function called np.mean() which will find the mean of any set of numbers you put in the parentheses

import seaborn as sns
import pandas as pd
import numpy as np

################## Data Structures ##################
# Data structures are ways that we represent information (data) in coding languages; today, we'll go over strings, integers/floats, lists, dictionaries
# Any data structure will be assigned to a variable. Variables are kinda like locations, we give them names but they hold information inside
    # Variables can't start with capital letters or numbers; they also can't contain symbols
    # It's helpful to use underscores (_) or capital lettering to indicate the starts of words

this_is_a_variable = "what's up"
thisIsAlsoAVariable = "nothing"
hereIs_anotherVariable = 'ok'

# STRINGS - these are words, numbers, symbols, spaces
    # these are always surrounded by '' or "" (doesn't make a difference most of the time which one you choose)

string_variable = 'this is a string'

# Integers and Floats - both are numbers, only difference is that floats can have decimals

integer_variable = 5
float_variable = 5.5

# LISTS - these are exactly how they sound, lists of data/information
    # Lists are always enclosed by brackets
    # Can contain any mix of data structures
    
list_variable = [1, 2, 3]
second_list = ['aleeza', 'noa', 'jessie', 'kayla']
third_list = [1, 'dog', 6.7]
list_list = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Can also create an empty list and "append" to it
empty_list = []
empty_list.append('new_value')
empty_list.append([1, 2])

# DICTIONARIES - think of dictionaries like a set of lockers, each has their own code (key) and hold data (values) within them
    # Dictionaries are always enclosed by these brackets {}
    # To create one, syntax is: {key : value}
        # Each can be any kind of data structure

dictionary_variable = {1 : 'january',
                       2 : 'february',
                       3 : 'march'}

second_dictionary = {'aleeza' : ['lab manager', 'VR study'],
                       'noa' : ['coordinator', 'meter', 'decnef'],
                       'jessie' : ['coordinator', 'YMAP'],
                       'kayla' : ['coordinator', 'exeter']}

# Another way to create dictionaries is to make an "empty" dictionary and fill it key by key

third_dictionary = {}
third_dictionary['key'] = 'value'

# We can collect a list of the keys and values (separately) by using the following methods
# These may look like lists but don't fully act like them. You can convert them into a list by using the list() function

dictionary_variable.keys() # this will return: dict_keys([1, 2, 3])
dictionary_variable.values() # this will return: dict_values(['january', 'february', 'march'])

# INDEXING - not a data structure but important tool for strings and lists
# this is how we pull specific items out of strings or lists
# every item in a list or character in a string has a position, unfortunately they all start at position 0

test_list = ["i'm first", "i'm second", "i'm third"]
first_item = test_list[0] # this sets first_item to "i'm first"

# You can also grab multiple items from these lists or strings using ":" between positions you want
# IMPORTANT - the end position is exclusive, meaning that it does not include that value in your output

test_string = 'blahblahIMPORTANTblahblah'
important = test_string[8:17]

# Also helpful to note that you can index from the back of the variable using negative values (-1). Unlike before, these don't start at 0 but -1
    # Going back to test_list above

third_item = test_list[-1]

################## basic functions ##################

# Functions are the tools we were talking about earlier, they let us do things easier and quicker; some are basic tools that we wouldn't be able to create otherwise
# Most functions have names which are immediately followed by parentheses. You put values inside to have it output anything.

print('hello ADRC')

range(1, 10)

list(range(1,10))

str(5)

len('southwest airlines')

type(5)

################## if elif and else statements/Conditional Statements ##################

# These are usually what you hear about with coding, they essentially help evaluate what to do
# They each check if something is True or False, then if it determines that something is True, it will execute whatever instructions you give it

study = 'TAD'

# "if" is always the first line for these
# Since we're not creating variables here, we have to use == instead of =. The computer won't understand why you're trying to create a variable

if study == 'meter':
    print('do you have social anxiety')
    
# you can have as many elif statements as you like, unlike the if and else statements

elif study == 'decnef':
    print('what animals are you afraid of')
    
elif study == 'YMAP':
    print('are you an adolescent')
    
# else essentially will be True if none of the other statements were evaluated to be True

else:
    print('this must be TAD')
    

# note - You can also just exclude else if you don't want anything to happen if the if/elif statements are all evaluated as False

# You can also check if multiple things are true in each if/elif statement
# Here, we can use "and" or "or" to check these conditions

# "and" example
# the entire if statement will be evaluated as True only if all criteria are met
# operators: <, >, !=

participant_id = 'tad8000'

if participant_id[0:3] == 'tad' and int(participant_id[-4:]) < 8000:
    print('this is an SMU TAD participant')
    
elif participant_id[0:3] == 'tad' and int(participant_id[-4:]) >= 8000:
    print('this is a UCLA TAD participant')
    
# "or" example
# the entire if statement will be evaluated as True if only one of the criteria are met

participant_id = 'dec100'

if participant_id[0:3] == 'tad' or participant_id[0:3] == 'dec' or participant_id[0:3] == 'met':
    print('this is a study at the ADRC')

################## for and while loops ##################

# I mostly use "for" loops but we'll cover "while" loops as well
# Loops are essentially instructions to your computer to repeat doing something until a condition is met

# WHILE loops - these are loops that will repeat your instructions infinitely until a condition (which you set) is met

x = 0

while x < 10:
    
    # this += essentially just adds 1 to the current value of x
    x += 1
    
    # i'll explain the f and the brackets
    print(f'{x} is not equal to 10')
    
    print('not done')
    
# FOR loops - these are loops that will repeat your instructions until it finishes cycling through the variable you give it

cycle = ['colors', 'whites', 'delicates', 'sheets']

for type in cycle:
    
    print(f'this is the {type} cycle')
    
# You can also do "nested" loops - these are loops within loops

for type in cycle:
    
    for percent in range(0, 101):
        
        if percent > 0:
            print(f'The {type} cycle is {percent}% complete')
            
        else:
            continue
        
#####################################################################################################################
