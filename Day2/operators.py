#try num = 8, or try num =10
# A small ticket system to show where to go depending on the ticket number
ticket_num = int(input("Enter the number on your ticket!"))
print('') #emptyline

if ticket_num > 10:
    print("Right here, welcome!")
else:
    print('Take a U turn!')

"""
also can do: Ternary operator
print('Right here!') if ticket_num > 10 else print('Take a U turn!')

"""