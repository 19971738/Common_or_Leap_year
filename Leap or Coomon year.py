year = int(input("Enter a year: "))

a = year % 4
b = year % 100
c = year % 400 

if year <= 1580:
    print("Not wihin the Gregorian calendar period")
elif a != 0:
    print("It's a common year")
elif b != 0:
    print("It is a lep year")
elif c != 0:
    print("It is a coomon year")
else: print("It is a leap year")
