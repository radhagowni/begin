year=int(input())
if (year%4==0 and year%100!=0 or year%400==0):
    print(year,' is leap year')
else:
    print(year,' non leap year')
print('another method by importing calendar')
import calendar
if calendar.isleap(year):
    print(year,'is leap year')
else:
    print(year,' not a leap year')
