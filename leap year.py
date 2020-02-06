n = int(input("enter the year:-"))
if n % 4 == 0:
    print("year is leap year")
    if n % 100 == 0:
        print("year is leap year")
        if n % 400 == 0:
            print("year is leap year")
else:
    print("year is not a leap year")
            
