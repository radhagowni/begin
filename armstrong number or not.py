n=int(input())
num=n
digit,sum=0,0
length=len(str(n))
for i in range(length):
    digit=int(num%10)
    num=num/10
    sum=sum+digit**length#pow(digit,length)
if sum==n:
    print('It is an armstrong number')
else:
    print('not an armstrong number')