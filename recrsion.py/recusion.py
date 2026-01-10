n=10
def number(n):
    if n==1:
        return
    print(n)
    number(n-1)

number(n)

