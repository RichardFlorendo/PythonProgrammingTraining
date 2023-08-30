class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def speak(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self. type = "dog"

    def speak(self):
        print(f"I am a Cat")

    def jump(self):
        print(f"Cat Jumping")


class Lion(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"I am a Lion")

    def jump(self):
        print(f"Lion Jumping")


myCat = Cat("Cathy", 3)
myCat.speak()
myCat.jump()

myLion = Lion("Lyonel", 4)
myLion.speak()
myLion.jump()