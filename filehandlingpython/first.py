# f=open('l00.html','x')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)
# w mode
# f=open('acpl.html','w')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# f.close()
# print(f.closed)
# print(f.encoding)
# apend mode 

# f=open('c.html','a')

# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)

# f=open('cbgty.html',"r")

# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)

# .method name variable*

# f=open('c20.py','x+')

# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)


# f=open('c.py','w+')

# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.readable())
# print(f.closed)
# print(f.encoding)


# single linr
# write krne ke liye 
# f= open("c.txt","a+")
# dat="this is python class"
# f.write(dat)
# f.close()

# f=open('l.txt','w')
# d="helo jatin"
# f.write(d)


# f=open('lp.txt','r')
# l=f.read()
# print(l)


# multiline


# f=open("lp.txt","a+")
# da="this is pyhton  " \
# "python class"
# f.write(da)
# f.close()


# next lines
# f=open("m.txt","a+")
# da="this is pyhton \n python class"
# f.write(da)
# f.close()

# mutipl elines

# coolection
# f=open("mm.txt","a+")
# d1="hello \n"
# d2="jatin \n"
# d3="how are you\n"
# f.writelines([d1,d2,d3])
# f.close()


# read () pure bit ke hisab

# wrieI()
# f=open("m.txt","r+")
# data=f.read()
# print(data)
# data1=f.read()
# print(data)
# print(data1)
# print(type(data1))

#   readr (n) by char

# f=open("m.txt","r+")
# data=f.read(1)
# print(data)
# data1=f.read(2)
# print(data1)
# print(data1)
# print(type(data1))

# read line()

# doubt
# data =f.readline()
# print(data)
# f.close()

# read lines


# data =f.readlines()
# print(data)
# f.close()


# curser movemnt e


# close athna
# with open 

# with open("c.txt","a+") as f:
#     data="python"
#     f.write(data)
#     print(f.closed)
# print(f.closed)

# cursor position of movement 

# tell seek 
# tell => it show cusor currnt position
# seek()=> thorgh this we moves our cursor to get required position


# tell():
# with open ("a.txt","a+") as f:
#     print(f.tell())
 
# with open ("a.txt","r+") as f:
#     print(f.tell())
#     data=f.read(10)
#     print(data)
#     print(f.tell())

# seek()

# with open("jatin.txt","ab+") as f:
#     print(f.tell())
#     data=b'hello friends'
#     f.write(data)
#     print(f.tell())
#     data1=f.read()
#     print(data1)
#     f.seek(0,0)
#     print(f.tell())
#     data1=f.read(20)
#     print(data1)
#     print(f.tell())

# rb+

# with open("jatin.txt","rb+") as f:
#     print(f.tell())
#     f.read(10)
#     print(f.tell())
#     f.seek(-5,1)
#     print(f.tell())
with open("p.docx","rb+") as f:
    print(f.tell())
    data10=f.read(10)
    print(data10)
    print(f.tell())
    f.seek(-5,1)
    print(f.tell())
    f.seek(10,1)
    print(f.tell())
    data4=f.read()
    print(data4)
    f.seek(-5,2)
    data1=f.read()
    print(data1)