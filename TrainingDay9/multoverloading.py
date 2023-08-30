class A:
    def show(self, a=None, b=None):
        print(a, b)

obj = A()
obj.show()
obj.show(4)
obj.show(2,5)


class Area:
    def find_area(self, a=None, b=None):
        if a is not None and b is not None:
            print("Area of Rectangle:", (a * b))
        elif a is not None:
            print("Area of Square:", (a * a))
        else:
            print("No values passed")

a1 = Area()
a1.find_area()
a1.find_area(3)
a1.find_area(4, 5)