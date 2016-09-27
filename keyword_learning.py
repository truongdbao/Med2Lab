from collections import defaultdict

# The inputs - each symptom is an item in the list
inputs = ["fever", "abdominal pain"]

case_data = open('pedcases_hawaii.txt' ,'r') # load the cases
keyword_data = open ('ped_symptoms', 'r') # load the keywords file

split_characters = "#######" # the characters used to split the contents of the

def haskeyword (key, str):
    if str.find(key) == -1 :
        return 0
    else:
        return 1



word_list = []

# Load the list of keywords into the keyword array

for word in keyword_data:
    word = word.rstrip()
    word_list.append(word)


occurrence = {}
for word in word_list:
    occurrence [word] = 0

for item in case_data.read().split(split_characters):
    count = 1
    for input in inputs :
        if haskeyword (input,item) == 0 :
            count = 0
            break
    if count == 1 :
        for word in word_list:
            if haskeyword (word,item) == 1:
                occurrence [word] = occurrence [word] + 1

print occurrence


top = []

for word in word_list:
    if not (word in inputs):
        if len(top) == 0 :
            top.append (word)
        else :
            i = 0
            while (i < len(top)) and (occurrence[top[i]] > occurrence[word]) :
                i = i + 1
            top.insert(i,word)


print '\n','Most common symptoms associated with',inputs,'are: \n '

i = 0
while i < 10:
    print top[i]
    i = i + 1










