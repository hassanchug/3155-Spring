# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramanian
# Links used for this exercise 
# https://www.kite.com/python/answers/how-to-find-common-elements-between-two-lists-in-python
# https://stackoverflow.com/questions/47454788/common-elements-between-two-lists-with-no-duplicates

list1 = []
list2 = []
list3 = []

def intersection():
    listset = set(list1)
    intersection = listset.intersection(list2)

for i in range(0,5): # stores first 5 ints in a list
    inputlist = int(input("Enter a number for the first list: "))
    list1.append(inputlist) 

for i in range(0,5): # stores second 5 ints in a list
    inputlist = int(input("Enter a number for the second list: "))
    list2.append(inputlist)

for i in list1: # third list to have common ints between the first two arrays
    if i in list2 and i not in list3:
        list3.append(i)
print(list3)
