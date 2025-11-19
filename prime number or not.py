# to check whether the number is a prime or not
n=int(input("Enter number:"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print(n,' is not prime')
else:
    print(n,' is prime')
    
