'''Import regex module'''
import re

#text = "the-stealth-warrior"
#text = "The_Stealth_Warrior"
TEST = "The_Stealth-Warrior"
#TEST = ""

def to_camel_case(text):
    '''The method/function so that it converts dash/underscore 
    delimited words into camel casing. The first word within 
    the output should be capitalized only if the original word
    was capitalized (known as Upper Camel Case, 
    also often referred to as Pascal case). 
    The next words should be always capitalized.
    Examples
    "the-stealth-warrior" gets converted to "theStealthWarrior"
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
    "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
    '''
    underscore = "_"
    dash = "-"
    pattern = "[-_]"
    replace = ' '

    if len(text) == 0:
        result = text
    else:
        if (underscore in text) or (dash in text):
            new_text = re.sub(pattern, replace, text)
            #print(new_text)
        new_list = re.split(replace, new_text)
        #print(new_list)
        for i, word in enumerate(new_list):
            if i == 0:
                continue
            else:
                new_list[i] = new_list[i].capitalize()
                #print(new_list[i])
        result = "".join(new_list)
    return result
print(to_camel_case(TEST))

"""
Alternative solution
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
"""