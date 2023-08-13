'''
For a given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
Input string: "The sunset sets at twelve o' clock."
Should return string: 
"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
'''

'''
Alternative solution #1:

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')
'''
'''
Alternative solution #2:

def alphabet_position(text):
    alphabet =  {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    inds = []
    for x in text.lower():
        if x in alphabet:
            inds.append(alphabet[x])
    return ' '.join(([str(x) for x in inds]))
'''

def alphabet_position(text):
    english_alphabet =  {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    # Convert input string to lowercase
    text = text.lower()
    # Variable to hold final string
    new_string = ""   
    # Loop letter by letter through the input string
    for l in text:
        # If it is a letter then, look it up in the dictionary and update final string with the key value. 
        # Otherwise, do nothing.
        if l in english_alphabet:
            # Appending number values and whitespace (last whitespace will have to be removed).
            new_string += str(english_alphabet[l]) + " "
    
    # After completing new string removing trailing whitespace before returning result.
    # https://geekflare.com/python-remove-last-character/
    final_string = ' '.join(new_string.split(' ')[:-1])
    return final_string

user_input = "The sunset sets at twelve o' clock."
print(alphabet_position(user_input))