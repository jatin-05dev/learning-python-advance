# decorator ek aise higher order function he jo arguemnt me function leta and return krta hec 
def dcor(fun_name):
    def inner(x,z):
        x=x+5
        z=z+5
        fun_name(x,z)
    return inner

    
@dcor
def add(x,z):
    print(x+z)


add(10,20)



# /2

def outerfun(var):
    def innerfun(x,y):
        x=x+5
        y=y+5
        var(x,y)
    return innerfun

@outerfun
def add(x,y):
    print(x+y)

add(45,5)

# even none


x=10
def outerfun(var):
    def innerfun(x):
        x=x+1
        var(x)
    return innerfun

@outerfun
def add(x):
    for i in range(1,x+1):
        print(2*i)
# even
n=10
def outerfun(var):
    def innerfun(x):        
        var(x)
        val=range(1,x+1,2)
        return list(val)
    return innerfun

@outerfun
def add(x):
        x=range(2,n+1,2)
        return list(x)


res=add(n)
print(res)

# odd



n=10
def outerfun(var):
    def innerfun(x):        
     return var(x)
    return innerfun

@outerfun
def add(x):
        x=range(2,n+1,2)
        return list(x)


res=add(n)
print(res)


