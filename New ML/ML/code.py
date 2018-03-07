# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:03:07 2018

@author: Surya
"""

import csv

flag = 0
intent1 = "NULL"
intent2 = "NULL"
intent3 = "NULL"
sen = raw_input("Please tell me your query \n")
if len(sen) >= 0:
    sen1 = sen
else:
    sen1 = "NULL"
    
words = sen1.split()
#print(words)
words.append(words)
#print(words)
max = (len(words)-1)
for x in range(0, max):
    csv_file = csv.reader(open('intent.csv'), delimiter=",")
    
    for row in csv_file:
        
        if words[x] == row[0]:
            intent1 = words[x]
            
            flag = flag+1

for y in range(0,max):
    csv_file1 = csv.reader(open('intent.csv'), delimiter=",")
    
    for row in csv_file1:
        
        if words[y] == row[1]:
            intent2 = words[y]
            flag = flag+1
            
            
intent3 = intent1+" "+intent2


if flag == 2:
    csv_file2 = csv.reader(open('answer.csv'), delimiter=",")
    for row in csv_file2:
        if intent3 == row[0]:
            print(row[1])
else:
    print("I am afraid I can't answer that.")
    
    