r=int(input("enter the number"))
def prime_number(n):
    status=True
    if n<2:
        status=False
    else:
        for i in range(2,n):
            if n%i==0:
                status=False
    return status
for n in range(1,r):
    if prime_number(n):
        print(n)
