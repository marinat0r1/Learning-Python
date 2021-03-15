import random

x = random.randint(0,9)
y = random.randint(0,9)
result = x*y

userinput = int(input("Baga: "))

if userinput == result:
    print("correct")
else:
    print("false, correct number is: ", result)