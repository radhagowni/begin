print('enter 3 numbers:')
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print('greatest number is',num1)
elif num2>num1 and num2>num3:
    print('greatest number is',num2)
else:
    print('the greatest number is',num3)
