import tkinter
from tkinter import messagebox
'''print("This program will allow you to input 3 numbers then determine which is the biggest among them")
num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(input("Input the third number: "))

if num1 > num2:
    if num1 > num3:
        print(f"The first number {num1} is bigger than the second number {num2} and the third number {num3}")
    else:
        print(f"Both the first and third numbers {num1} are equal and bigger then the second number {num2}")
elif num2 > num1:
    if num2 > num3:
        print(f"The second number {num2} is bigger than the first number {num1} and the third number {num3}")
    elif num2 == num3:
        print(f"Both the second and third numbers {num2} are equal and bigger then the first number {num1}")
    else:
        print(f"The third number {num3} is bigger than the first number {num1} and the second number {num2}")
elif num3 > num1:
    if num3 > num2:
        print(f"The third number {num3} is bigger than the first number {num1} and the second number {num2}")
elif num1 == num2 and num1 != num3 and num2 != num3:
    print(f"Both the first and second numbers {num1} are equal and bigger then the third number {num3}")
elif num1 == num2 and num1 == num3 and num2 == num3:
    print("All the numbers are equal")
else:
    print("Incorrect input")'''

'''response = messagebox.askokcancel("Ok Cancel Message Box", "Okay or Cancel?")
if response:
    messagebox.showinfo("Okay", "You clicked Okay")
else:
    messagebox.showinfo("Cancelled", "You clicked Cancel")

response = messagebox.askyesno("Yes No Message Box", "Yes or No?")
if response:
    messagebox.showinfo("Yes", "You clicked Yes")
else:
    messagebox.showinfo("No", "You clicked No")

response = messagebox.askretrycancel("Retry Cancel Message Box", "Retry or Cancel?")
if response:
    messagebox.showinfo("Retry", "You clicked Retry")
else:
    messagebox.showinfo("Cancelled", "You clicked Cancel")

response = messagebox.askyesnocancel("Yes No Cancel Message Box", "Yes, No, or Cancel?")
if response == True:
    confirm = messagebox.askokcancel("Yes", "You clicked Yes. Confirm?")
    if confirm:
        messagebox.ask("Confirmed", "Thank you for Confirming")
    else:
        messagebox.showinfo("Stopping", "Stopping the process")
elif response == False:
    messagebox.showinfo("No", "You clicked No")
elif response == None:
    messagebox.showinfo("Cancel", "You Cancelled the transaction")'''

'''print("This program will display the multiplication table of a number that you input until the 10th multiple")
number = int(input("Input the number you want to use: "))

for multiple in range(1, 11):
    print(str(multiple), "times", number, "=", multiple * number)'''

'''foodlist = ["Ice Cream", "Chocolate", "Frappe"]

print("Normal List:")
for normalList in foodlist:
    print(normalList)

print("\nSorted List:")
for sortedList in sorted(foodlist):
    print(sortedList)

print("\nReversed List:")
for revList in reversed(foodlist):
    print(revList)

print("\nEnumerated List:")
for enumList in enumerate(foodlist):
    print(enumList)

print("\nEnumerated List with Position and Index:")
for pos, item in enumerate(foodlist):
    print(f"The element in index {pos + 1} is the food {item}")'''

'''students = ["Smith, John", "Carter, Andrew", "Anderson, Robert", "White, Betty"]

for index, element in enumerate(sorted(students)):
    print(f"Student Number {index + 1}: {element}")'''

'''startIndex = 0
while startIndex < 10:
    print(startIndex)
    startIndex = startIndex + 1

carIndex = 0
carList = ["BMW", "Audi", "Subaru", "Nissan"]
while carIndex < len(carList):
    print(carList[carIndex])
    carIndex = carIndex + 1'''

'''carIndex = 0
carList = ["BMW", "Audi", "Subaru", "Nissan"]
while carIndex < len(carList):
    if carList[carIndex] == "Subaru":
        break
    else:
        print(carList[carIndex])
    carIndex = carIndex + 1'''

'''while True:
    insert = input("Type 'q' to stop the program")
    if insert == "q":
        print("Program stopped")
        break'''

'''for hundred in range (1, 101):
    if hundred % 5 == 0 and hundred % 3 == 0:
        print("FizzBuzz")
    elif hundred % 3 == 0:
        print("Fizz")
    elif hundred % 5 == 0:
        print("Buzz")
    else:
        print(hundred)

pizza = []
print("This program will ask you to input toppings on a pizza until you quit")
while True:
    topping = input("Input your pizza topping. Input 'q' to quit.")
    if topping == "q":
        print("You quit the program\n")
        print(f"Your pizza is ready with the following toppings: ")
        for toppingList in range(0, len(pizza)):
            print(pizza[toppingList])
        break
    else:
        print(f"Okay, I will add {topping} on your pizza\n")
        pizza.append(topping)'''

price = 0
print("This program will tell you the price of the ticket and total them all after quitting")
while True:
    age = input("Input your age. Input 'q' to Quit")
    if str(age) == "q":
        print(f"Your total ticket price is ${price}")
        break
    else:
        if int(age) <= 3:
            print("Your ticket is free")
        elif int(age) > 3 and int(age) <= 12:
            print("The ticket is $10")
            price += 10
        elif int(age) > 12:
            print("The ticket is $15")
            price += 15
        else:
            print("Invalid Input")