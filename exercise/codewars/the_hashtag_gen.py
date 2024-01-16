def generate_hashtag(s):
    #your code here
    # If string is empty then, return false.
    if len(s) == 0:
        return False
    else:
        # Capitalize every first letter of every word.
        new_s = s.title()
        # Remove every matching character from a string.
        new_s = new_s.replace(" ","")
        # Add hashtag at the beginning of the string.
        new_s = "#" + new_s
        
        # If the final string is longer than 140 char then, return false.
        if len(new_s) > 140:
            return False
        else:
            return new_s

'''
# Alternative solution
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
'''
