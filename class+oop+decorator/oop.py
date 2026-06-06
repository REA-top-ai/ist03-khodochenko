def zadanie_1():
    class Employee:
        new_id = 1
        
        def __init__(self):
            self.id = Employee.new_id
            Employee.new_id += 1
            
        def say_id(self):
            print(f"My id is: {self.id}")

    e1 = Employee()
    e2 = Employee()
    e1.say_id()
    e2.say_id()


def zadanie_2():
    class Employee:
        new_id = 1
        def __init__(self):
            self.id = Employee.new_id
            Employee.new_id += 1
        def say_id(self):
            print(f"My id is: {self.id}")

    class Admin(Employee):
        pass

    e3 = Admin()
    e3.say_id()


def zadanie_3():
    class Employee:
        new_id = 1
        def __init__(self):
            self.id = Employee.new_id
            Employee.new_id += 1
        def say_id(self):
            print(f"My id is: {self.id}")

    class Admin(Employee):
        def say_id(self):
            print("I am an Admin")

    e3 = Admin()
    e3.say_id()


def zadanie_4():
    class Employee:
        new_id = 1
        def __init__(self):
            self.id = Employee.new_id
            Employee.new_id += 1
        def say_id(self):
            print(f"My id is: {self.id}")

    class Admin(Employee):
        def say_id(self):
            super().say_id()
            print("Salam, I am an Admin")

    e3 = Admin()
    e3.say_id()

print("\n", "zadanie_1:")
zadanie_1()
print("\n", "zadanie_2:")
zadanie_2()
print("\n", "zadanie_3:")
zadanie_3()
print("\n", "zadanie_4:")
zadanie_4()
