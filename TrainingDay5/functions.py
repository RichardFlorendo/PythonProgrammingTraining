import math
import random

# Continued from TrainingDay4

'''heroes = {
    'Batman': {
        'Strength': 8,
        'Speed': 5,
        'Stamina': 6,
        'Luck': 3
    },
    'Robin': {
        'Strength': 6,
        'Speed': 9,
        'Stamina': 8,
        'Luck': 7
    }
}

villains = {
    'Joker': {
        'Strength': 4,
        'Speed': 7,
        'Stamina': 3,
        'Luck': 7
    },
    'Bane': {
        'Strength': 9,
        'Speed': 4,
        'Stamina': 7,
        'Luck': 4
    }
}

print("This program will let you choose Heroes and Villains and see who wins in which categories")
hchoice = input("Choose your Hero: Batman or Robin?").title()

for key, values in heroes.get(hchoice).items():
    print(key + " : " + str(values))

vchoice = input("Choose your Villain: Joker or Bane?").title()

for key, values in villains.get(vchoice).items():
    print(key + " : " + str(values))

heroCount = 0
villainCount = 0

while True:
    print("Which category do you choose for this fight?")
    for key in heroes.get('Batman'):
        print("- " + key)

    print("Or send 'quit' to exit the program")

    choice = input("Choose the category: ").title()

    heroStat = heroes.get(hchoice).get(choice)
    villainStat = villains.get(vchoice).get(choice)

    if choice == "Quit":
        print("\n****************************")
        if heroCount > villainCount:
            print(hchoice + " wins the battle!")
        elif villainCount > heroCount:
            print(vchoice + " wins the battle!")
        else:
            print("The battle between " + hchoice + " and " + vchoice + " is a draw.")

        print("****************************\n")
        break

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if heroStat > villainStat:
        print(hchoice + " wins the " + choice + " battle.")
        heroCount += 1
    elif villainStat > heroStat:
        print(vchoice + " wins the " + choice + " battle.")
        villainCount += 1
    else:
        print(hchoice + " and " + vchoice + " draws the " + choice + " battle.")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")'''

'''def some_message():
    print("This is some message that I am printing out.")

some_message()

def subtraction(first_number, second_number):
    print("The Subtrahend is: ", first_number)
    print("The Minuend is: ", second_number)
    diff = first_number - second_number
    print(diff)

subtraction(5, 3)

def subtracting(subtrahend, minuend):
    difference = subtrahend - minuend
    return difference

differenceTotal = subtracting(10, 3)
print(differenceTotal)'''

'''def addition(number1, number2):
    sum = number1 + number2
    print("The sum of", number1, "and", number2, "is", sum)


def subtraction(number1, number2):
    diff = number1 - number2
    print("The difference of", number1, "and", number2, "is", diff)


def multiplication(number1, number2):
    product = number1 * number2
    print("The product of", number1, "and", number2, "is", product)


def division(number1, number2):
    quotient = number1 / number2
    print("The quotient of", number1, "and", number2, "is", quotient)


print("This program will calculate the two numbers you input to whichever operation you choose:")
first = int(input("Input the first number: \n"))
second = int(input("Input the second number: \n"))

print("Choose the operation to perform with the numbers:\n "
      "1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division")
choice = int(input("Which operation do you choose?\n"))

if choice == 1:
    addition(first, second)
elif choice == 2:
    subtraction(first, second)
elif choice == 3:
    multiplication(first, second)
elif choice == 4:
    division(first, second)
else:
    print("Invalid input, try again later")'''

'''def circle(radius):
    perim = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return perim, area


def square(side):
    perim = 4 * side
    area = side ** 2
    return perim, area


def rectangle(length, width):
    perim = 2 * (length + width)
    area = length * width
    return perim, area


print("This program will calculate the area and perimeter of your chosen shape:")

choice = int(input("Choose the shape:\n 1 - Circle\n 2 - Square\n 3 - Rectangle\n"))

if choice == 1:
    number = float(input("Input the radius of the circle:\n"))
    perim, area = circle(number)
    print("The perimeter of the circle is", perim, "and the area of the circle is", area)
elif choice == 2:
    number = float(input("Input the length of one side of the square:\n"))
    perim, area = square(number)
    print("The perimeter of the square is", perim, "and the area of the square is", area)
elif choice == 3:
    number1 = float(input("Input the length of the rectangle:\n"))
    number2 = float(input("Input the width of the rectangle:\n"))
    perim, area = rectangle(number1, number2)
    print("The perimeter of the rectangle is", perim, "and the area of the rectangle is", area)
else:
    print("Invalid input, try again later")'''

'''def calculation(number, overtime=False):
    total = ((number * 8) * 5) * 30
    #total = number * 10
    if overtime:
        total += (total / 2)
    return total


print("This application will calculate the salary of your employee:\n")

name = input("Input the name of your employee:\n")
salary = int(input("Input the hourly salary of your employee in AED\n"))
over = input("Does " + name + " have any overtime?\n").title()

if over == "Yes":
    output = calculation(salary, True)
else:
    output = calculation(salary)

print("The overall salary of", name, "is", output)'''

'''guessCount = 0

number = random.randint(1, 10)
name = input("Hello, what is your name?\n")

print("I am thinking of a number between 1 - 10, what do you think it is?")

while guessCount != 5:
    guess = int(input())

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    elif guess == number:
        break
    else:
        print("Invalid input")

    guessCount += 1

if guess == number:
    print("Congratulations", name, "you guessed the number", number, "in", guessCount, "tries!")
else:
    print("You failed to guess the number in 5 tries. Better luck next time!")'''


def student(name, id):
    print(f"Student name is {name.title()} and ID is {id}")


student("John", 12)


def employee(empname, empid):
    print(f"The Employee's name is {empname.title()} and ID is {empid}")


employee(empid=1001, empname='Mark')


def greet_users(names):
    for name in names:
        print("Welcome, " + name)


names = ['Adam', 'Cain', 'Abel']
greet_users(names)


def studentsample(name, id, course='BSC CC'):
    student_name = {'name':name, 'id': id, 'course': course}
    return student_name

name = studentsample('Luke', 1234)
print("The details of the student are:")
for key, value in name.items():
    print(key, ":", value)

name = studentsample('Luke', 1234, 'Python')
print("The details of the student are:")
for key, value in name.items():
    print(key, ":", value)