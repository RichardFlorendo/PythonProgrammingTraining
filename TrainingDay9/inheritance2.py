class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        #self.name = name
        #self.age = age
        self. type = "dog"

myDog = Dog("Doug", 2)
myDog.speak()