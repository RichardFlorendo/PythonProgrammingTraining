class Person:
    def __init__(self):
        self.name = "Richard Florendo"

    def bio(self):
        self.addr = "Abu Dhabi, UAE"
        self.taxInfo = "SAMPLEDATA134"
        self.contact = "123456"
        print(self.addr, self.taxInfo, self.contact)

    def interest(self):
        self.favFood = "Spicy"
        self.hobbies = "Games"
        self.bloodType = "A+"
        print(self.favFood, self.hobbies, self.bloodType)

obj = Person()
print(obj.name)
#obj.bio()
obj.interest()