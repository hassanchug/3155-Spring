# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramanian
#https://www.quora.com/How-do-you-write-a-Python-program-that-takes-inputs-from-the-user-until-q-is-entered-Do-you-have-to-make-a-list-from-user-inputs

list1 =[]
evenList = [] # creates the lists 


while True:
    entry = input("Enter a number or QUIT to quit: ")
    if entry == "QUIT": # if QUIT is typed then the system will break
        break
    
    list1.append(int(entry)) # appends all entered values to a list

for x in list1: # adds only even numbers to another list and print 
    if x % 2 == 0:
        evenList.append(x)



print(evenList)