def zadanie_1():
    class Facade:
        pass

def zadanie_2():
    class Facade:
        pass
    
    facade_1 = Facade()
    return facade_1

def zadanie_3():
    class Facade:
        pass
    
    facade_1 = Facade()
    facade_1_type = type(facade_1)
    print(facade_1_type)
    
    return facade_1_type

def zadanie_4():
    class Grade:
        minimum_passing = 65
    
    print(f"Minimum passing grade: {Grade.minimum_passing}")
    return Grade

def zadanie_5():
    class Rules:
        def washing_brushes(self):
            return "Point bristles towards the basin while washing your brushes."
    
    rules_instance = Rules()
    print(rules_instance.washing_brushes())
    return Rules

def zadanie_6():
    class Circle:
        pi = 3.14
        
        def area(self, radius):
            return self.pi * radius ** 2
            
    circle_instance = Circle()
    radius_val = 5
    print(f"Area of circle with radius {radius_val}: {circle_instance.area(radius_val)}")
    return Circle


zadanie_1()
zadanie_2()
print("\n","zadanie_3:")
zadanie_3()
print("\n","zadanie_4:")
zadanie_4()
print("\n", "zadanie_5:")
zadanie_5()
print("\n","zadanie_6:")
zadanie_6()
