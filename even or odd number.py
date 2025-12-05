# if any number is divisible by 2 then it is even
num=int(input('Enter num:'))
if (num%2==0):
    print(num,' even number')
else:
    print(num,' odd number')
#alternate method
print('Alternate method output :')
print('even number' if num%2==0  else "odd number")
