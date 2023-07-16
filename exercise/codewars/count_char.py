'''Function to count occurances of a character in a string.

Alternative solution:
from collections import Counter

def count(string):
    return Counter(string)
'''

def count(s):
    '''Function to count occurances of a character in a string.'''
    dict_1 = {}

    if len(s) == 0:
        return dict_1
        #return {}
    else:
        for l in s:
            if l in dict_1:
                dict_1[l] = dict_1.get(l) + 1
            else:
                dict_1[l] = 1
        return dict_1

user_input = input()
print(count(user_input))
