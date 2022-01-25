# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramanian
# Links used for this exercise 
# https://stackoverflow.com/questions/12887042/python-using-set-to-create-list-of-elements-that-only-appear-once

from collections import Counter

x = []
y = []

for i in range(0, 10):
    nnums = int(input("Enter a number: "))
    x.append(nnums) # appends user inputted elements to the first list 

for item, count in Counter(x).most_common(): # finds most common elements and only prints the unique elements 
    if count == 1: 
        y.append(item)

print(y)

