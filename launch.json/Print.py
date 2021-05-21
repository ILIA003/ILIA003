a = int(input()) 
b = int(input()) 
c = int(input()) 
sum = 0
if a < 0:
    a = 0
if b < 0:
    b = 0
if c < 0:
    c = 0
if a > 0:
    sum = a + c + b
if b > 0:
    sum = a + c + b
if c > 0:
    sum = a + c + b
print(sum) # самое главное чтобы к переменной приравнять 0 это здесь типо как связующее между со всеми операторами