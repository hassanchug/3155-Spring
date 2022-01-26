# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# Links used for this exercise 
# https://www.w3schools.com/python/python_howto_reverse_string.asp


# Takes in a string and slices it backwards
def rev_func(x):
  return x[::-1]

# Function call to unput a string
text = rev_func(input("Enter a string: "))

# Prints the reversed output
print(text)
