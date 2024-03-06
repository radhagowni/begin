num1=int(input('enter number:'))
num2=int(input('enter number:'))
if num1>num2:
    print('greater number is',num1)
else:
    print('greater number is',num2)
print('alternate method:')
print('greater number is',max(num1,num2))
print('one more method:')
print(num1 if num1>num2 else num2 )