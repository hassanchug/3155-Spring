# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# Links used for this exercise 
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/#:~:text=In%20Python%2C%20lower()%20is,it%20returns%20the%20original%20string


# Asks the user to input a string
user_input = input("Enter a string: ")  

# creates a list for the lowercase and uppercase letters
lowercase = [] 
uppercase = []

# Changes all the lowercase letters into uppercase
lowercase = [l for l in user_input if l.islower()]
# Changes all the uppercase to lowercase
uppercase = [l for l in user_input if l.isupper()]

# sorts lowercase letters before uppercase letters
reversed = (lowercase + uppercase)
for i in reversed:
    print(*i, sep = '', end ='')

print("\n")
    