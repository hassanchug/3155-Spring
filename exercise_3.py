# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramanian
# Link used for this exercise 
# https://kodify.net/python/math/square/ 

from math import sqrt

squarenum = int(input("Enter a numebr greater than 1: ")) 

k = 0

for x in range(0, squarenum + 1): 
    if k >= 0:
        print("The square of", k, "is", k ** 2) # prints the square of the inputed number 
        k = k + 1
    else:
        print("Invalid input, please enter a number greater than 1: ")
        break
