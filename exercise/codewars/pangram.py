"""A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. Ignore numbers and punctuation."""

user_input = "The quick brown fox jumps over the lazy dog"

#english_alphabet =  [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
english_alphabet_2 =  {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

def is_pangram(s):
    for l in user_input:
        if l in english_alphabet_2:
            english_alphabet_2.update({l:english_alphabet_2[l] + 1})

    #print("Dictionary values are = ",english_alphabet_2.values())

    if 0 in english_alphabet_2.values():
        return Flase
    else:
        return True

a = is_pangram(user_input)

"""
def is_pangram(s):
    english_alphabet_2 =  {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    user_input = s.lower()
    for l in user_input:
        if l in english_alphabet_2:
            english_alphabet_2.update({l:english_alphabet_2[l] + 1})

    print("Dictionary values are = ",english_alphabet_2.values())

    if 0 in english_alphabet_2.values():
        return False
    else:
        return True
"""

"""
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
"""