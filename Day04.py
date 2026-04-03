a = 7
b = 3
c = "42"
d = 7.0
e = True

print(type(a / b))       # 1. float default
print(type(a // b))      # 2. int traditional way.. of wanting int to be the div value
print(a + e)             # 3. 8 (7+ true means 1 = 8)
print(type(c + str(a)))  # 4. str type of c is str and we convert a int to str and then add. 
print(c + str(a))
print(a == d)            # 5. True compares content 
print(a is d)            # 6. false -- do both point to same object in memory? No. 
print(int(c) + a)        # 7. 49
print(float(e))          # 8. 1.0
