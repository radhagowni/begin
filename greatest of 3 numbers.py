#this program is to find the greatest numbers among 3 numbers
print('Enter 3 numbers:')
num1=int(input("Enter number 1:"))
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print('Greatest number is',num1)
elif num2>num1 and num2>num3:
    print('Greatest number is',num2)
else:
    print('The greatest number is',num3)
