# first exception 
# try:
#   x=10
#   y=0
#   d=x/y
#   print(d)
# except:
#   print("ni hoga")
# sexcond multipleexception

# try:
#     x=int(input("enter a number 1"))
#     y=int(input("enter a number 2"))
#     z=x/y
#     print(z)
# except ZeroDivisionError:
#     print("shi daal")
# except ValueError:
#     print("string nhi ")
# else:
#     print("thik")
# finally:
#     print("hogayag")    

# hard custome exception

class overage(Exception):
    pass

def checkage(age):
    if age<18:
        raise overage("nabalik he tu")
    else:
        print("shi aja")
    
try:
    n=int(input("enter : "))
    checkage(n)
except overage as e:
    print(e)
    
print("checker ...........")
    
