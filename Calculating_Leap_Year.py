#
#
#A program that determines whether a given year is a leap year.
#
#Must satisfy the conditions:
#Multiple of 400
#Multiple of 4 and not multiple of 100

year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("\n"+str(year)+" is a leap year.\n")
else:
    print("\n"+str(year)+" is not a leap year.\n")

