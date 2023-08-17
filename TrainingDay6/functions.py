'''def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = 5
print("The factorial of ", num)
res = fact(num)
print("is ", res)

addTwenty = lambda x: x + 20
print(addTwenty(5))

sumFour = lambda w, x, y, z: w + x + y + z
print(sumFour(1, 2, 3, 4))


setNums = {101, 124, 31, 23}
print(setNums)

mixedSet = {'Sample', 34, -1, 43.21, True}
print(mixedSet)

setNums.add(193)
print("New nums set after add: ", setNums)

setNums.discard(101)
print("New nums set after discard:", setNums)


setA = {2, 3, 5}
setB = {1, 2, 6}

print("Union using |:", setA|setB)
print("Union using union():", setA.union(setB))

setA = {1, 3, 5}
setB = {1, 2, 3}

print("Intersection using &:", setA&setB)
print("Intersection using intersection():", setA.intersection(setB))

setA = {2, 3, 5}
setB = {1, 2, 6}

print("Difference using &:", setA-setB)
print("Difference using difference():", setA.difference(setB))

vowels = ['a', 'e', 'i', 'o', 'u']
fset = frozenset(vowels)

print("The frozen set is:", fset)

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

C = A.copy()
print(C)

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))'''

'''print("This program will determine the Permutation of the numbers you input")
n = int(input("Input the number of elements in the set: "))
r = int(input("Input the number of subsets of the set: "))


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


perm = fact(n) / fact(n - r)
comb = fact(n) / fact(n - r) * fact(r)

print("The permutation is: ", perm)
print("The combination is: ", comb)'''
'''#number = input("Enter a number")

try:
    number = int(input("Enter a number"))
    print("Your number is: ", number)
except:
    print("Wrong Input")'''

STotal = 0
DTotal = 0


def snackOptions():
    while True:
        try:
            choice = int(
                input("Choose your snack:\n 1. Snickers(1.5)\n 2. Twix(3.0)\n 3. M&Ms(1.0)\n 4. Lays(4.0)\n 5. Return"))
            if choice == 1:
                print("Snickers has been added\n")
                return + 1.5
            elif choice == 2:
                print("Twix has been added\n")
                return + 3.0
            elif choice == 3:
                print("M&Ms has been added\n")
                return + 1.0
            elif choice == 4:
                print("Lays has been added\n")
                return + 4.0
            elif choice == 5:
                break
        except:
            print("Invalid input, try again")


def drinkOptions():
    while True:
        try:
            choice = int(input("Choose your drink:\n 1. Coke(1.5)\n 2. Iced Tea(3.0)\n 3. Water(1.0)\n 4. Return"))
            if choice == 1:
                print("Coke has been added\n")
                return + 1.5
            elif choice == 2:
                print("Iced Tea has been added\n")
                return + 3.0
            elif choice == 3:
                print("Water has been added\n")
                return + 1.0
            elif choice == 4:
                break
        except:
            print("Invalid input, try again")


def payment(snackTotal, drinkTotal):
    total = snackTotal + drinkTotal
    print("Your total is ", total)

    while True:
        payment = float(input("Please input your payment here: "))
        try:
            if payment >= total:
                print("Thank you for your payment, your change is: ", payment - total)
                break
            else:
                print("Insufficient amount, please try again")
        except:
            print("Invalid input")


print("*********** Vending Machine ************")
while True:
    try:
        choice = int(input("Hello, what would you like today?\n 1. Drinks\n 2. Snacks\n 3. Payment"))
        if choice == 1:
            DTotal += drinkOptions()
        elif choice == 2:
            STotal += snackOptions()
        elif choice == 3:
            payment(STotal, DTotal)
            break
    except:
        print("Invalid input")
