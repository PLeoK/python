"""
def my_min(x, y, *args):
    counter = 0
    for i in args:
        if x < args[counter]:
            print(x)
        else:
            print(args[counter])
        counter += 1
        #print(i)

print(my_min(8, 13, 4, 42, 120, 7))
"""
def my_min(*args):
    return min(args)

print(my_min(8, 13, 4, 42, 120, 7))