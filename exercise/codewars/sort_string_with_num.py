'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
'''
def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)
'''
'''
def sort_string_by_number(input_string):
    if not input_string:
        return ""

    def extract_number(word):
        for char in word:
            if char.isdigit():
                return int(char)
        return None

    words = input_string.split()
    sorted_words = sorted(words, key=extract_number)
    return " ".join(sorted_words)

# Example usage:
input_string = "word2 word1 word3 word9 word5 word8 word4 word7 word6"
sorted_string = sort_string_by_number(input_string)
print(sorted_string)  # Output: "word1 word2 word3 word4 word5 word6 word7 word8 word9"
'''