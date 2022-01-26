# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

user_input = input("Enter a string: ")

lowercase = []
uppercase = []

lowercase = [l for l in user_input if l.islower()]
uppercase = [l for l in user_input if l.isupper()]

reversed = (lowercase + uppercase)
for i in reversed:
    print(*i, sep = '', end ='')
    
print("\n")
    