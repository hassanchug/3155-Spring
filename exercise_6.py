# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramanian
# Links used for this exercise
# https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20.

rownum = int(input("Enter a row num from 1 to 5: "))
columnnum = int(input("Enter a col num from 1 to 5: "))

grid = [([0] * 5) for i in range(5)]  # take in a row and column entered by the user
grid[rownum - 1][columnnum - 1] = 1

for i in grid: # print out grid from the row and column that was entered
    print(*i, sep = ' ')