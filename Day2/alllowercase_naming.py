#the filename shows how we generally name the python files, no spaces, use underscore. 
#Literal assignment

first = "Dave"
last = "Game"

print(first, last)
print(type(first))
print(type(last))
print(type(first)== str)
print(type(last)== int)
print(isinstance(first, str))
print(isinstance(last, float))

#constructir function assignment

pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza)== str)
# print(isinstance(pizza, str))

#Concatenation
fullname = first + " " + last + "Orders pizza" + pizza
print(fullname)

#casting a number to a string
decade = str(1980)
print(f'decade is a :{type(decade)}')

statement = "I like music from " + decade + "s."
print(statement)

#Multiple lines
multiline = '''
Hey, how are you?

I was just checking in. 

                all good??? 
'''
print(multiline)

#escaping special characters: use backslash
sentence = 'I\'m a new \\born babyyyy yayyyy!\tHey\nseriously\ duhhh? ' #observe output carefully
print(sentence)

#string methods
mySentence = "ILOOKOLDTOYOU!!!!!HELLOOO"
mySentence2 = "hellodoilooksmall????"
print(mySentence.lower()) #lowercase
print(mySentence2.upper()) #uppercase
print(multiline.title()) #titlecase, cap every word
print(mySentence.center(50)) #adds padding
print(mySentence.casefold()) #
print(mySentence.count('O'))# countsn number of given string alphabet
print(mySentence.endswith('I')) #returns boolean if anything returns true or false
print(mySentence.replace('LOOK', ' -sadly I was replaced- '))
print(len(mySentence))
mySentence = "                       " + mySentence+"                  "
print(len(mySentence))
print(mySentence.strip())

print(mySentence.rstrip())

print(mySentence.lstrip())



