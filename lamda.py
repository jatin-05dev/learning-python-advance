# ans=lambda x,y :x+y
# print(ans(100,200))

# x=10
# loop=lambda x : print("even") if x%2==0 else print("odd") 
# loop(x)


# l=[1,2,3,4,5,6,7,8,9]
# print(list(map(lambda x:x*2,l)))


# l=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x: x % 2 == 0, l)))


# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9]
# print((reduce(lambda x,y:x+y,l,0)))


from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
print((reduce(lambda x,y:x if x>y else y,l)))

