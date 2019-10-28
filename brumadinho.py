import csv
import re


a = 'Brumadinho'     #String that you want to search

with open("log.csv") as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    for line in reader:      #Iterates through the rows of your csv
        result = re.match(r"Brumadinho", line)
        with open('palavras.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('title', 'intro'))
            writer.writerows(result)
            
            