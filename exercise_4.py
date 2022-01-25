# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramanian
# Links used for this exercise 
# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
# https://www.geeksforgeeks.org/find-average-list-python/

from statistics import mean

def Average(list):
    return mean(list)

list = []
k = 1
 
n = int(input("Enter a number: "))

for i in range(0, n):
    numbernums = float(input("Enter number " + str(k) + ": ")) #Takes the input and makes sure its the number the user will have to enter
    list.append(numbernums)
    k = k + 1

mean = Average(list) # creates list of all number and gets a average
print("List:", list)
print("Average:", mean)
