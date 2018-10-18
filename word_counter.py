from tkinter.filedialog import askopenfilename
import string

file_object = open(askopenfilename(), 'r')
test_string = file_object.read()


word_list = test_string.split()

for word in word_list:
    for char in word:
        if char in string.punctuation and char != "'":
            word.replace(char, "")

word_dict = {}
for word in word_list:
    word_dict[word] = 0

for word in word_list:
    word_dict[word] += 1

for word in sorted(word_dict, key=word_dict.get, reverse=True):
    print(word, word_dict[word])
