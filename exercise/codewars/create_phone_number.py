"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number. 
"""

def create_phone_number(n):
    """
    Function o convert list of integers to list of strings using map().
    Returns format: "(123) 456-7890"
    """
    s = list(map(str, n))

    s.insert(0, '(')
    s.insert(4, ')')
    s.insert(5, " ")
    s.insert(9, "-")
    return "".join(s)

#n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
n = [12, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(create_phone_number(n))

# Alternative solution #1
#def create_phone_number(n):
#	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# Alternative solution #2
#def create_phone_number(n):
#    n = ''.join(map(str,n))
#    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])
