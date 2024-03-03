num=int(input('enter num:'))
if (num%2==0):
    print('even number')
else:
    print('odd number')
#alternate method
print('alternate method output :')
print('even number' if num%2==0  else "odd number")