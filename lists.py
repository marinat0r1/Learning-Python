exlist1 = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
exlist1.append(10)
print(exlist1[4:])

for i in range(len(exlist1)):
    print(exlist1[i])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitsWithA = [x for x in fruits if "a" in x]
print(fruitsWithA)

def isThereACherry(args):
    if "cherry" in args:
        print("There is a cherry wohoo")
    else:
        print("No cherry here :(")

isThereACherry(fruits)
isThereACherry(exlist1)

# lambdas ??