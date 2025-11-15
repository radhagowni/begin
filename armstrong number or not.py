#this program is to check whether the given number is armstrong number or not
n=int(input())
num=n
digit,sum=0,0
length=len(str(n))
for i in range(length):
    digit=int(num%10)
    num=num/10
    sum=sum+digit**length  # alternate method for this line is using pow(digit,length) function
if sum==n:
    print(n,' is an armstrong number')
else:
    print(n,' not an armstrong number')
