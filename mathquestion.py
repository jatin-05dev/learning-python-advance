# python question all test ke liye 

# leap year 

year =int(input("enter a year"))

if (year%4==0 and year%100!=0) or (year%400==0):
    print("leaop year")
else:
    print("nota leapyaer")\

# sunny number

number =int(input("enter anumber : "))
aage=number+1

i=1
while i*i<=aage:
    if i*i==aage:
        print("sunny number")
        break
    i=i+1
else:
    print("not a sunny number")

import math
number=int(input("enter anumber: "))
aage=number+1
sq=math.sqrt(aage)
if(sq*sq==aage):
    print("sunny numbrr")
else:
    print("not sunny number")
# spy number

number =int(input("enter anumber : "))
num=number
sum=0
pr=1
while number>0:
    r=number%10
    sum=sum+r
    pr=pr*r
    number=number//10


if(pr==sum):
    print("spy")
else:
    print("not spy")


# peter son number

 
n = int(input("Enter how many terms: "))

n2=n
sum=0
while n2>0:
    rem=n2%10
    fac=1
    for i in range(1,rem+1):
        fac=fac*i
    sum=sum+fac

        
    n2=n2//10


if n==sum:
    print("peter")
else:
    print("not petre")

# neon

n = int(input("Enter how many terms: "))
n1=n
r=n*n
sum=0
while r>0:
    rem=r%10
    sum=sum+rem
    r=r//10


if n1==sum:
    print("neon num")
else:
    print("not neon")

# anagram

st=input("enter string")
st2=input("enter string2")

if sorted(st)==sorted(st2):
    print("ana")
else:
    print("not ana")

# harsahd

n = int(input("Enter how many terms: "))
n1=n
s=0
while n>0:
    r=n%10
    s=s+r 
    n=n//10


if(n1%s==0):
    print("harshad")

else:
    print("not harshad")

# fibonacci series
num=int(input("enter a number : "))
fir=0
sec=1
nex=0
i=1
while i<num:
    fir=sec
    sec=nex
    nex=fir+sec
    print(fir)
    i=i+1


# lcm and hcf 
number1 =int (input("enter number 1 : "))
number2 =int (input("enter number 2 : "))

i=1
hcf=1
lcm=1
while i<=number1 and i<=number2:
    if(number1 % i ==0 and number2 %i==0):
        hcf=i
    i=i+1

lcm=number1*number2//hcf



print(hcf," ",lcm)

# lcm pure

number1 =int (input("enter number 1 : "))
number2 =int (input("enter number 2 : "))
lcm2=max(number1,number2)

while True:
    if(lcm2%number1==0 and lcm2%number2==0):
        break
    lcm2=lcm2+1

print(lcm2)
# palindrome

n=int(input("ennter s anumber"))
n2=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10

if(rev==n2):
    print("palindrome")

else:
    print("not palindrome")

# py


s=input("enter a string : ")
rev=s[::-1]
int(rev)
print(rev)


# palinfrome string

s=input("enter a string : ")
s2=""
a=len(s)
for i in range(a-1,-1,-1):
    s2=s2+s[i]


print(s2)

# slice

s=input("enter a string : ")
print(s[::-1])

