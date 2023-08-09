'''name = "Richard"
search = "id"
if search in name:
    print("Search term found")
else:
    print("Search term not found")

sampleText = input("Input your First name and Last name")
returnValue = sampleText.find(' ')
if returnValue != -1:
    fName = sampleText[:returnValue]
    lName = sampleText[returnValue + 1:]
    print(lName + ", " + fName)
else:
    print("Error")'''

'''text = "abcdefghijklmnop"
textCount = len(text)
print(textCount)

text = "This this this is a sample of this"
textSearch = text.count("this")
print(textSearch)

sample = " Richard "
stripText = sample.strip()
leftStrip = sample.lstrip()
rightStrip = sample.rstrip()
print(stripText)
print(leftStrip)
print(rightStrip)


text = "Richard Edmund Richard"
stripText = text.strip("Richard")
leftStrip = text.lstrip("Richard")
rightStrip = text.rstrip("Richard")
print(stripText)
print(leftStrip)
print(rightStrip)'''

'''superheroes = ["Ironman", "Spider-Man", "Batman", "Superman"]
print("Choose your favorite hero among these:\n 1. Ironman\n 2. Spider-Man\n 3. Batman\n 4. Superman")
choice = int(input("Input your choice here: "))
result = choice - 1
print(f"You chose: {superheroes[result]}")'''

'''menu = ["Chicken Curry", "Beef Biryani", "Fried Chicken with Fries", "Lamb Chops"]
print(f"Choose your meal among these:\n 1. {menu[0]}\n 2. {menu[1]}\n 3. {menu[2]}\n 4. {menu[3]}")
choice = int(input("Input your choice here: "))
result = choice - 1
print(f"Your order of {menu[result]} is being prepared in the kitchen now")'''

'''menu = ["Chicken Curry", "Beef Biryani"]
menu2 = ["Fried Chicken with Fries", "Lamb Chops"]
print(menu + menu2)'''

'''menu = ["Chicken Curry", "Beef Biryani", "Fried Chicken with Fries", "Lamb Chops"]
menu.append("Beef Stew")
menu.insert(1, "Samosas with Dip")
print(menu)

removed = menu.pop(2)
print(f"The removed item is: {removed}\n")

del menu[2]
print(menu)

menu.remove("Chicken Curry")
print(menu)'''

'''menu = ["Chicken Curry", "Beef Biryani", "Fried Chicken with Fries", "Lamb Chops"]
newMenu = menu[:2]
print(newMenu)

menu[:] = []
print(menu)

answer = int(input("How old are you now? "))

if answer == 25:
    print("You are 25 years old")
else:
    print("You are not 25 years old")

age = int(input("How old are you? "))

if age <= 0:
    print("Input a number more than 0")
elif age > 25:
    print("You are older than 25 years old")
elif age < 25:
    print("You are younger than 25 years old")
else:
    print("You are 25 years old")

response = int(input("How old are you? "))

if response <= 0:
    print("Input a number more than 0")
elif 0 < response < 13:
    print("You are a kid")
elif 12 < response < 20:
    print("You are a teenager")
elif 19 < response < 60:
    print("You are an adult")
else:
    print("You are old")'''

'''print("Input your grades below and I will calculate your grade")
mathin = int(input("Math: "))
sciin = int(input("Science: "))
histin = int(input("History: "))

total = (mathin + sciin + histin) / 3

if total <= 60:
    print(f"Your average is {total} and you get an F. See you next year!")
elif total > 60 and total <= 70:
    print(f"Your average is {total} and you get a D. Try better next time!")
elif total > 70 and total <= 80:
    print(f"Your average is {total} and you get a C! Nice!")
elif total > 80 and total <= 90:
    print(f"Your average is {total} and you get a B! Good Job!")
else:
    print(f"Your average is {total} and you get an A! Congrats!")'''

'''trafficColor = input("What color is the traffic light now?")

if trafficColor == "green" or trafficColor == "Green" or trafficColor == "GREEN":
    print("You may go.")
elif trafficColor == "yellow" or trafficColor == "Yellow" or trafficColor == "YELLOW":
    print("Slow down and stop at the traffic light.")
elif trafficColor == "red" or trafficColor == "Red" or trafficColor == "RED":
    print("You should wait for the traffic light to turn Green.")
else:
    print("That is not one of the colors of a Traffic Light")'''

'''age = int(input("Enter your age:"))

if age >= 13 and age <= 21:
    if age == 13:
        print("You are a new teenager")
    else:
        print("You are a teenager aged between 14 and 21")
else:
    print("You are not a teenager")'''