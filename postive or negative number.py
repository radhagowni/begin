num=int(input('enter a number:'))
if num>=0:
    if num>0:
        print(num," positive number")
    else:
        print('0')
else:
    print(num,' negative number')
#alternate method
print('alternate method output:')
print('positive' if num>=0 else 'negative')
