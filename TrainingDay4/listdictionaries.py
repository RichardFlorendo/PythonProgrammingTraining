'''tuple1 = ('Zelda', 'MonHun', 'FE', 'Skyrim')

for person in tuple1:
    print(person)

print("Number One", tuple1[0])
print("Top Two", tuple1[:2])

final_tuple = tuple1[0] + tuple1[2]
print("Final Two:", final_tuple)
'''

'''player = {'Name': 'McStabby', 'Role': 'Rogue', 'Strength': 6, 'Luck': 9, 'Stamina': 7}
for key, value in player.items():
    print(key, ":", value)

for key in player.keys():
    print(key)

for value in player.values():
    print(value)

name = player.get('Name')
print(name)

enemy = {}
enemy['Name'] = "Evilman"
enemy['Role'] = "BBEG"
enemy['Strength'] = 9
enemy['Luck'] = 5
enemy['Stamina'] = 6

for key, values in enemy.items():
    print(key, ":", values)

count = 0

print("*******************")
print(player.get('Role'), "vs", enemy.get('Role'))
print("*******************")

if enemy.get('Stamina') > player.get('Stamina'):
    print("BBEG Wins the Stamina Battle")
elif enemy.get('Stamina') == player.get('Stamina'):
    print("The Stamina Battle is a Draw")
else:
    print("Rogue Wins the Stamina Battle")
    count += 1

print("*******************")

if enemy.get('Luck') > player.get('Luck'):
    print("BBEG Wins the Luck Battle")
elif enemy.get('Luck') == player.get('Luck'):
    print("The Luck Battle is a Draw")
else:
    print("Rogue Wins the Luck Battle")
    count += 1

print("*******************")

if enemy.get('Strength') > player.get('Strength'):
    print("BBEG Wins the Strength Battle")
elif enemy.get('Strength') == player.get('Strength'):
    print("The Strength Battle is a Draw")
else:
    print("Rogue Wins the Strength Battle")
    count += 1

print("*******************")

if count >= 2:
    print(player.get('Name'), "the", player.get('Role'), "defeats", enemy.get('Name'), "the", enemy.get('Role'))
elif count == 0:
    print(player.get('Name'), "the", player.get('Role'), "draws with", enemy.get('Name'), "the", enemy.get('Role'))
else:
    print(enemy.get('Name'), "the", enemy.get('Role'), "defeats", player.get('Name'), "the", player.get('Role'))'''

'''student1 = {'Name': 'John', 'ID': 45, 'Course': 'BSC'}
student2 = {'Name': 'Mark', 'ID': 1, 'Course': 'BA'}
student3 = {'Name': 'Luke', 'ID': 14, 'Course': 'STEM'}
student4 = {'Name': 'Paul', 'ID': 27, 'Course': 'BSC'}

student = [student1, student2, student3, student4]

for std in student:
    for key, value in std.items():
        print(key, ":", value)
    print("*******************")

student = {
    'name': 'Timothy',
    'marks': ['Mathematics - 80', 'Science - 85']
}

print(f"{student['name']} scored the following marks:")
for mark in student['marks']:
    print(mark)

cities = {
    'dubai':{
        'country': 'UAE',
        'population': 3500000,
        'Famous for': 'Burj Khalifa'
    },
    'paris': {
        'country': 'france',
        'population': 11000000,
        'Famous for': 'Eiffel Tower'
    },
    'Agra': {
        'country': 'India',
        'population': 2000000,
        'Famous for': 'Taj Mahal'
    }
}

for city, city_info in cities.items():  
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['Famous for'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("\tIt has a population of about " + str(population) + ".")
    print("\tAnd is famous for " + fact + ".")'''

heroes = {
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
    print(key, values)

vchoice = input("Choose your Villain: Joker or Bane?").title()

#Completed in TrainingDay5 File