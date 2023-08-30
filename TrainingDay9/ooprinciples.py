'''class Employee:
    employeeCount = 0
    def __init__(self, name, salary):
        self.name = name
        Employee.employeeCount += 1
        self.salary = salary

    def displayEmployees(self):
        print(f"The employee's name is {self.name} and they have a monthly salary of {self.salary} AED per month")


while True:

    nam = input("Input the name of the employee or send 'quit' to end")
    if nam == "quit":
        break
    sal = int(input("Input the monthly salary of the employee"))
    employee = Employee(name=nam, salary=sal)
    employee.displayEmployees()
print(f"You have {Employee.employeeCount} total employees")'''


