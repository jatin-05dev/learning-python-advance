# # decorator ek aise higher order function he jo arguemnt me function leta and return krta hec 
# def dcor(fun_name):
#     def inner(x,z):
#         x=x+5
#         z=z+5
#         fun_name(x,z)
#     return inner

    
# @dcor
# def add(x,z):
#     print(x+z)


# add(10,20)



# # /2

# def outerfun(var):
#     def innerfun(x,y):
#         x=x+5
#         y=y+5
#         var(x,y)
#     return innerfun

# @outerfun
# def add(x,y):
#     print(x+y)

# add(45,5)

# # even none


# x=10
# def outerfun(var):
#     def innerfun(x):
#         x=x+1
#         var(x)
#     return innerfun

# @outerfun
# def add(x):
#     for i in range(1,x+1):
#         print(2*i)
# # even
# n=10
# def outerfun(var):
#     def innerfun(x):        
#         var(x)
#         val=range(1,x+1,2)
#         return list(val)
#     return innerfun

# @outerfun
# def add(x):
#         x=range(2,n+1,2)
#         return list(x)


# res=add(n)
# print(res)

# # odd



# n=10
# def outerfun(var):
#     def innerfun(x):        
#      return var(x)
#     return innerfun

# @outerfun
# def add(x):
#         x=range(2,n+1,2)
#         return list(x)


# res=add(n)
# print(res)
 
def deco(fun):
    def inner(n):
        print("Odd numbers:")
        for i in range(1, n+1, 2):
            print(i)
        fun(n)
    return inner


@deco
def even(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)  # even ka code ignore ho jayega


n = int(input("Enter a number: "))
even(n)




# def decorator(fun):
#     def wrapper(data):
#         ans = fun(data)
#         print(ans)  
#         return ans/len(data)
#     return wrapper


# @decorator
# def addition_of_list(data):
#     ans=0
#     for i in data:
#         ans+=i
#     return ans


# li = [1,23,5,62]
# ans = addition_of_list(li)
# print(ans)





