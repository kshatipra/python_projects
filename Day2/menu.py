#Build A menu

title = "menu".upper()
print(title.center(20, "=")) #"=" any char you pass fills the rest of the space
print("Coffee".ljust(16,".")+"$1".rjust(4))
print("Muffin".ljust(16,".")+"$4".rjust(4))
print("CheeseCake".ljust(16,".")+"$4".rjust(4))
print("Tea".ljust(16,".")+"$6".rjust(4))

print("")

#string index values
title = "WORLDISLOVE"
print(title[1])
print(title[-1])
print(title[1:8])
print(title.startswith("W")) #true
print(title.endswith("Q")) #false

#Boolean Data types
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

#numericData Types

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float
gpa = 9.87809
#similar

#complex
comp_value = 5+ 3j
print(type(comp_value))
print(comp_value.imag)
print(comp_value.real)
print(comp_value.conjugate())

#Built-in-functions for numbers

print(abs(gpa)) #rounds to the nearest integer
print(round(gpa,2)) #rounds to the nearest decimal you specify
print(round(gpa)) #rounds

import math #imporst should be to the top of the python page
print(math.pi) #prints pi value
print(math.degrees(100)) #calculate radians to degrees 
print(math.sqrt(47)) #prints square root

# zipcode1 = 0192283 #error : if it is num, must not start with 0, else mut be a string, try uncommenting
# print(zipcode1)
zipcode = "09126790"
zip_value = int(zipcode)
print(type(zip_value))

#zip_value = int("I am prentending to be an integer but shh I am a string!") #throwws error, as you caste incorrect value to int