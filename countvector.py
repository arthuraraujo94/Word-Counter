from tkfilebrowser import askopenfilename
import string
import json
import csv
from sklearn.feature_extraction.text import CountVectorizer

file_object = open(askopenfilename(), 'r')
test_string = file_object.read()
file = open('testfile.txt','w') 

text = file

vectorizer = CountVectorizer()
x= vectorizer.fit_transform(text)
z= vectorizer.get_feature_names()

print(z)
print('\n',x.toarray())