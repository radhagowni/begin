# greatest number among 2 numbers
num1=int(input('enter number:'))
num2=int(input('enter number:'))
if num1>num2:
    print('Greater number is',num1)
else:
    print('Greater number is',num2)
print('alternate method:')
print('Greater number is',max(num1,num2))
print('one more method:')
print(num1 if num1>num2 else num2 )
