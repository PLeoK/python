"""
Given two integers a and b, which can be positive or negative, 
find the sum of all the integers between and including them and return it. 
If the two numbers are equal return a or b.
Note: a and b are not ordered!
Your function should only return a number, not the explanation about how you get that number.
Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
"""

def get_sum(a,b):
    """Docstring"""
    input_list = []
    input_list.append(a)
    input_list.append(b)
    input_list.sort()
    #print(input_list)
    num_sum = 0
    for num in range(input_list[0],input_list[-1] + 1):
        #print (num)
        num_sum += num
        #print(sum)
    return sum

# Alternative approach
#def get_sum(a,b):
#    return sum(range(min(a, b), max(a, b) + 1))
