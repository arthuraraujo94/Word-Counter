from tkfilebrowser import askopenfilename
import string
import json
import csv


file_object = open(askopenfilename(), 'r')
test_string = file_object.read()
file = open('testfile.txt','w')
stopwords = open('stopwords.txt', 'w') 

word_list = test_string.split()

with open ('resultadobrumadinho.csv', 'w') as output:
    fieldnames = ['palavra', 'contagem']
    writer = csv.DictWriter(output, fieldnames=fieldnames)

    writer.writeheader()
    
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
        writer.writerow({'palavra': word, 'contagem': word_dict[word]})
      
    
    

input("\nPress ENTER to quit.")
