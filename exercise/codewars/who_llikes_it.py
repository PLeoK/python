def likes(names):
    # your code here
    if len(names) == 0:
         #print("no one likes this")
            return "no one likes this"
    elif len(names) == 1:
        name = names[0]
        #return f,"{name} likes this"
        return "{} likes this".format(name)
    elif len(names) == 2:
        name0 = names[0]
        name1 = names[1]
        return "{} and {} like this".format(name0, name1)
    elif len(names) == 3:
        name0 = names[0]
        name1 = names[1]
        name2 = names[2]
        return "{}, {} and {} like this".format(name0, name1, name2)
    else:
        others_num = len(names) - 2
        name0 = names[0]
        name1 = names[1]
        return "{}, {} and {} others like this".format(name0, name1, others_num)

"""
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
"""
