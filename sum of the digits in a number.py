num=int(input('enter a number:'))
sum=0 
while num!=0:
    digit=int(num%10)
    sum=sum+digit
    num=num/10
print('sum of the digits in given number: ',sum)
