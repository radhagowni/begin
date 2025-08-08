num=int(input('enter num:'))
if (num%2==0):
    print(num,' even number')
else:
    print(num,' odd number')
#alternate method
print('alternate method output :')
print('even number' if num%2==0  else "odd number")
