# class parent:
#     city="bhopal"
#     def car(self):
#         print("car from parent")
# class child(parent):
#     pass
# obj=child()

# print(obj.city)
# obj.car()


# single level inheritance
# overiding jisme ek hi method use kra ho use method overiding bolte
# same method i'n two diffrent clas which have inheritance  
class parent:
    car="mercedes"
    def home(self):
            print("home from patrent")

class child (parent):
    car="audi"
    car2=parent.car
    def home(self):
        super().home()
        print(parent.car)
        print(super().car)
        print("HOME FROM child")
        
            
# obj=child()
# print(obj.car)
# print(obj.car2)
# obj.home()


# # multi level inheritance
# class granparent:
#     car="mercedes"
#     def home(self):
#             print("home from gp")

# class parent(granparent):
#     bank="sbi"
#     def land(self):
#         print("land FROM parent")

# class child(parent):
#      pass
        
            
# obj=child()
# print(obj.car,obj.bank)
# obj.land()
# obj.home()

# multiple inheritance
# mro means method resolution orde/r

# class father:
#     def  home(self):
#         print("home from father")
# class mother:
#     def car(self):
#         print("car from mother")
#     def home(self):
#         print("home from mother")
# class child(mother,father):
#     pass
        

# obj=child()
# obj.car()
# obj.home()
# sab do

# extra
# class father:
#     def  home(self):
#         print("home from father")
# class mother:
#     def car(self):
#         print("car from mother")
#     def home(self):
#         print("home from mother")
#         father.home(self)

# class child(mother,father):
#     pass 
# obj=child()
# obj.car()
# obj.home()
# class father:
#     def  home(self):
#         print("home from father")
#         mother.home(self)

# class mother:
#     def car(self):
#         print("car from mother")
#     def home(self):
#         print("home from mother")

# class child(father,mother):
#     pass
        

# obj=child()
# obj.car()
# obj.home()
# heiirachical inheritance
# class parent:
#     def home(self):
#         print("home from parent")
#     def car(self):
#         print("car feom parent")
# class child1(parent):
#     pass
# class child2(parent):
#     pass
    
# obj1=child1()
# obj2=child2()

# obj1.car()
# obj2.car()
# obj1.home()
# obj2.home()

# hybrid
# class grandfather:
#     def home(self):
#         print("home from grand father")
#     def car(self):
#         print("car from grand father")

# class father(grandfather):
#     def bank(self):
#         print("cash from fathetr")
# class mother(grandfather):
#     def land(self):
#         print("land from mother")

# class child(father,mother):
#     pass
        

# obj1=child()
# obj1.car()
# same

# class grandfather:
#     def home(self):
#         print("home from grand father")
#     def car(self):
#         print("car from grand father")

# class father(grandfather):
#     def bank(self):
#         print("cash from fathetr")
#         mother.bank(self)
    

# class mother(grandfather):
#     def bank(self):
#         print("cash from mother")


# class child(father,mother):
#     pass
        

# obj1=child()
# obj1.bank()      
# polymorphism isi ek function opertor ka ek se jyda from hoi 

# class stu:
#     pass

# print(dir(stu))

# method overloading means same name and same class and different para metre  and this is not supported in poly inheritance me krta he
# overload me ko fir call nhi krta aur ovid krne ke liye variable length argyue
# class stu:
#     def add(x,y,*ar):
#         print(x+y)
#     def add(x,y,z):
#         print(x+y+z)
#     def add(x,y,z,p):
#         print(x+y+z+p)

# obj=stu
# obj.add(10)
# obj.add(10,10,10,10)

# avoid


# class stu:
#     def add(ṣelf,*ar):
#         print(ar)
    

# obj=stu()
# obj.add(10)
# obj.add(10,10,10,10)



# abstraction 
# from abc import ABC,abstractmethod
# class cal(ABC):
#     def add(self,a,b):
#         print(a+b)
#     def sub(self,a,b):
#         print(a-b)
#     def mul(self,a,b):
#         print(a*b)
#     @abstractmethod
#     def div(self):
#         pass
# class junior(cal):
#     def div(self,a,b):
#         print(a//b)
         

# obj=junior()
# obj.add(2,8)
# obj.mul(2,8)
# obj.div(2,8)


# encapsulation me public variable

# class earth:
#     name="world"
#     def add(self):
#         print("hello")
# class plan(earth):
#     pass

# obj=plan()
# print(obj.name)
# obj.add()

# protetd

# class earth:
#     _name="world"
#     def _add(self):
#         print("hello")
# class plan(earth):
#     pass

# obj=plan()
# print(obj._name)
# obj._add()

# private

# class earth:
    # __name="world"
    # def __add(self):
        # print("hello")
# class plan(earth):
    # pass

# obj=plan()
# print(obj.__name)
# obj.__add()
# print(earth.__name)
# print(dir(earth))
# obj._earth__add()
# print(obj._earth__name)


