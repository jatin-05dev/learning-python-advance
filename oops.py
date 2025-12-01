# ------------------------------------------
# OOPS Practical Program (All in One File)
# ------------------------------------------

from abc import ABC, abstractmethod

# 1. Encapsulation + Constructor + Instance Variables
class Student:
    def __init__(self, name, marks):
        self.name = name          # public
        self._marks = marks       # protected
        self.__secret = "Hidden"  # private

    def display(self):
        print(f"Name: {self.name}, Marks: {self._marks}")

# 2. Inheritance
class Person:
    def speak(self):
        print("Person is speaking...")

class Teacher(Person):   # Single Inheritance
    def speak(self):      # Method Overriding (Polymorphism)
        print("Teacher is teaching...")

# 3. Multiple Inheritance
class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):
    def showC(self):
        print("Class C")

# 4. Abstraction
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# 5. Class Variable + Static Method
class MathUtils:
    pi = 3.14  # class variable

    @staticmethod
    def add(a, b):
        return a + b


# ------------------------------------------
# MAIN PROGRAM (Testing Everything)
# ------------------------------------------

print("\n--- Student Class (Encapsulation) ---")
s1 = Student("Jatin", 88)
s1.display()

print("\n--- Inheritance & Polymorphism ---")
t1 = Teacher()
t1.speak()

print("\n--- Multiple Inheritance ---")
obj = C()
obj.showA()
obj.showB()
obj.showC()

print("\n--- Abstraction Example (Area of Circle) ---")
c = Circle(5)
print("Circle Area:", c.area())

print("\n--- Static Method + Class Variable ---")
print("Add:", MathUtils.add(10, 20))
print("Value of PI:", MathUtils.pi)
