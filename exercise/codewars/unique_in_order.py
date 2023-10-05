def unique_in_order(sequence):

    # initialize a null list
    unique_list = []
    if len(sequence) == 0:
        return unique_list
    if len(sequence) == 1:
        unique_list.append(sequence[0])
        return unique_list
    
    #l = []
    counter = 0
    for item in sequence:
        #if item not in l:
        if counter == 0:
            unique_list.append(item)
        if counter != 0:
            if item != sequence[counter-1]:
                unique_list.append(item)
        counter += 1
    return unique_list

# Alternative solution
#def unique_in_order(iterable):
#    result = []
#    prev = None
#    for char in iterable[0:]:
#        if char != prev:
#            result.append(char)
#            prev = char
#    return result
