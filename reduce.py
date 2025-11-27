# import functools
# l=[1,2,3,4,5,6,7]
# def sum(x,y):
#     print(x,y)
#     return x+y


# res=functools.reduce(sum,l,0)
# print(res)

# sum

# import functools
# l=[1,2,3,4,5,6,7]
# def sum(x,y):
#     print(x,y)
#     return x+y


# res=functools.reduce(sum,l)
# print(res)

# max



# import functools
# l=[1,2,3,4,15,6,7]
# def sum(x,y):
#     if(x>y):
#         return x
#     else:
#         return y


# res=functools.reduce(sum,l)
# print(res)


# lamda

# x=lambda p,q,r: p+q+r 
# # print(x(10,10,10))
# z=x(8,7,5)
# print(z)


# return


# x=lambda p,q,r:return p+q+r 
# # print(x(10,10,10))
# z=x(8,7,5)
# print(z)

# x=lambda p,q,r: print(p+q+r) 
# x(4,5,8)
# print(x(10,10,10))
# z=x(8,7,5)
# print(z)
# chota krne ke lye 
# x=lambda p,q: p if p>q else q 
# print(x(10,10,10))
# print(x(10,20))


#  map with lamda
# l=[1,12,8,4,-5]
# print(list(map(lambda n: n*n ,l)))
# print(list(map(lambda n: "even" if n%2==0 else "odd",l)))
# filtet with map
# print(list(filter(lambda n:n if n%2==0,l)))
# print(list(filter(lambda n:n if n%2!=0 else None,l)))
# reduce unlamda
# from functools import reduce
# print(reduce(lambda x,y:x*y,l))
# print(reduce(lambda x,y:x if x>y else y,l))
# print(reduce(lambda x,y:x if y>x else x,l))
# second max
# us=int(print("enter yoou want"))
# la=reduce(lambda x,y:x if x>y else y,l)
# l.remove(la)
# print(l)
# print(reduce(lambda x,y:x if x>y else y,l))
# n=int(input("enter a number which you eant : "))
# if n<=len(l):
#     for _ in range(n):
#         x=reduce(lambda x,y:x if x>y else y,l)
#         l.remove(x)
#     print(f'{n} max  {x}')
# else:
#     print("enter valid")
# min
# n=int(input("enter a number which you eant : "))
# if n<=len(l):
#     for _ in range(n): vvv                          
#         x=reduce(lambda x,y:x if x<y else y,l)
#         l.remove(x)
#     print(f'{n} max  {x}')
# else:
#     print("enter valid")












