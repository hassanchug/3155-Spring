# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramanian
# Links used for this exercise
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

user_string = input("Enter a string: ")
user_string = str(user_string)

def split(user_string): #split function to split into single characters 
    return list(user_string)
user_string = (split(user_string))

n = 3 # each list has only 3 elements 
split_list = [user_string[i * n:(i +1) * n] for i in range ((len(user_string) + n - 1) // n)] # splits into the single characters seperated by commas and brackets 
print(split_list)