import csv
from googletrans import Translator
import time

translator = Translator()

f = open('Subway-Seoul-ver-2.csv', 'r', encoding='euc-kr')
f2 = open('Subway-Seoul-Eng-ver-2.csv', 'w', encoding='utf-8', newline='\n')

reader = csv.reader(f)
writer = csv.writer(f2)

dic = {}
for line in reader:
    print(line)

    if line[0] not in dic.keys():
        dic[line[0]] = translator.translate(line[0]).text

    if line[1] not in dic.keys():
        dic[line[1]] = translator.translate(line[1]).text

    newline = [dic[line[0]], dic[line[1]],int(line[2])]

    print(newline)
    writer.writerow(newline)

    time.sleep(3)

f.close()
f2.close()