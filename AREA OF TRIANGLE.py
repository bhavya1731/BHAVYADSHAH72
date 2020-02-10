a=int(input('ENTER THE 1ST SIDE OF TRIANGLE: '))
b=int(input('ENTER THE 2ND SIDE OF TRIANGLE: '))
c=int(input('ENTER THE 3RD SIDE OF TRIANGLE: '))
p=a+b+c
print('parimeter of triyangle',p)
s=p/2;
a=(s*(s-a)*(s-b)*(s-c))**(1/2)
print('AREA OF TRIANGLE',a)


