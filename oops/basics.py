# basics class

class Stu:
    name="pooja"
    def  __init__(self):
        print("called");

obj=Stu()
print(obj.name)
print(id(obj))
obj2=Stu()
print(id(obj2))
print(dir(obj2))
print(Stu.__doc__)
print(Stu.__module__)
print(Stu.__dict__)
print(Stu.__init__)





