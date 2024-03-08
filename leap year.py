year=int(input())
if (year%4==0 and year%100!=0 or year%400==0):
    print(year,'is leap year')
else:
    print('non leap year')
print('another method by importing calender')
import calendar
if calendar.isleap(year):
    print(year,'is leap year')
else:
    print('not a leap year')