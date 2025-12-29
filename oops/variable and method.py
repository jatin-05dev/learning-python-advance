# instance var object dependent
# declaration inside a class
# class Stu:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(name,age)
#     def play(self,playing):
#        self.playing=playing        
# obj=Stu("pooja",25)
# obj2=Stu("sonam",33)
# print(obj.name,obj2.name)
# obj.play("cricket")
# obj.play("gili")
# declaration outside a class
# class Stu:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj=Stu("jatin",55)
# obj.salary=555520000
# print(obj.name)
# print(obj.salary)
# obj2=Stu("jatin",5520)
# obj2.salary=555
# print(obj2.salary)

# class variable common in all 
# inside the object 
# class Stu:
#     school="gnps"

# obj=Stu()
# obj.school="hh"
# print(obj.school)
# outside the object
# class Stu:
#     pass 

# Stu.city="BHOPAL"
# obj=Stu()
# print(obj.city)

# local variables are local and cant acceess

# class Stu:
#     def __init__(self,name,roolno):
#         self.n=name
#         self.r=roolno
#         x=55
#         print(x)
#     def show(self):
#         y=4956
#         print(y)
      
 
# obj=Stu("jatin",897)
# obj.show()


# methods types in classess 

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def show(self):   # instance method
#         print(self.name)

# s = Student("Aman")
# s.show()

# class method

# class Student:
#     school = "DPS"

#     @classmethod
#     def change_school(cls):
#         cls.school = "KV"

# Student.change_school()
# print(Student.school)



# class BOOK:
#     price = 666           # class variable

#     def __init__(self, title, branch):
#         self.t = title
#         self.b = branch

#     @classmethod
#     def uc(cls, newp):   # class method properly class ke andar
#         cls.price = newp

# # Object
# obj = BOOK("python", "it")
# print(obj.price)        # 666

# x = float(input("Enter new price: "))
# obj.uc(x)               # works now
# print(obj.price)        # updated value


# blobk direct access nhi hp skta (())




# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Math.add(2, 3))


# class Stu:
#     x=45
#     def __init__(self, name):
#         self.name = name

#     @staticmethod   
#     def show():
#         print(Stu.x)

        
# obj=Stu("jatin")
# obj.show()

# 
# greet


# class Stu:
#     x=45
#     def __init__(self, name):
#         self.name = name

#     @staticmethod   
#     def show(name):
#         print(f"welcome {name}")

        
# obj=Stu("jatin")
# x=obj.name
# obj.show(x)


