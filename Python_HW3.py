import re

original_text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# number of whitespaces
ws = 0
for i in original_text:
    if (i.isspace()):
        ws += 1
print("Number of whitespaces: ", ws)

# number of spaces
spaces = original_text.count(' ')
print("Number of spaces: ", spaces, '\n')

# normalization of letter height
norm = original_text.capitalize()
# print (norm)

# fixing whitespaces
a1 = norm.replace("\n", "")
fws = a1.replace("  ", "\n")
# print (fws)

# fixing misspelling in the text
b1 = fws.replace("iz ", "is ")
b2 = b1.replace("tex.", "text.")
fms = b2.replace("x“iz", "x “iz")
# print (fms)

# gathering the new sentence with last word of each sentence
c1 = fms.split('.')
c1.pop()
for i in range(len(c1)):
    c1[i] = str(c1[i])
    c1[i] = c1[i].split()[-1]
    new_sentence = ' '.join(c1) + "."
# print(new_sentence)

# adding new sentence to general text
gen_text = fms + '\n'*2 +"aditional sentence:" + '\n' + new_sentence
# print(gen_text)

# insert capital letters
d1 = list(gen_text)
for i in range(len(d1) - 1):
    if d1[i] == ".":
        d1[i + 2] = d1[i + 2].upper()
    elif d1[i] == "\n":
        d1[i + 1] = d1[i + 1].upper()
    homework = ''.join(d1)
print(homework)
