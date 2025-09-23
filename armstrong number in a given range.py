#this program is to print the armstrong numbers in the given range
low=int(input())
high=int(input())
for n in range(low,high+1):
    temp=n
    order=len(str(n))
    sum=0  
    while temp >0:
        digit=temp%10
        temp=n//10
        sum=sum+pow(digit,order)
    if sum==n:
        print('Armstrong numbers are:')
        print(n,end='  ')
    
