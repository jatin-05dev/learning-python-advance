# ===============================
# OOPS CONSTRUCTOR – ALL IN ONE FILE
# ===============================

# 1️⃣ Basic Constructor
class A:
    def __init__(self):
        print("Basic Constructor called")

obj1 = A()


# 2️⃣ Parameterized Constructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 20)
print(s1.name, s1.age)


# 3️⃣ Default Constructor using default values
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p1 = Person()
p2 = Person("Aman", 22)
print(p1.name, p1.age)
print(p2.name, p2.age)


# 4️⃣ Constructor + Method
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print(self.brand, self.price)

c1 = Car("BMW", 5000000)
c1.show()


# 5️⃣ Constructor Overloading (Trick using default value)
class Demo:
    def __init__(self, x=None):
        self.x = x
        print("Value:", self.x)

d1 = Demo()
d2 = Demo(10)


# 6️⃣ Constructor in Inheritance
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

c = Child()


# 7️⃣ Parameterized Constructor in Inheritance
class Father:
    def __init__(self, name):
        self.name = name

class Son(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

s = Son("Raj", 18)
print(s.name, s.age)


# 8️⃣ Private Variable in Constructor
class Test:
    def __init__(self):
        self.__x = 100   # private variable

    def show(self):
        print(self.__x)

t = Test()
t.show()


# 9️⃣ Real-life Example (Bank)
class Bank:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient balance")

b = Bank(1234, 1000)
b.deposit(500)
b.withdraw(300)
print("Final Balance:", b.balance)


# 🔟 Destructor (Extra)
class Sample:
    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")

s = Sample()
del s
