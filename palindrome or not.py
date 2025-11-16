n=int(input("Enter number:"))
temp=n
reverse=0
while temp>0:  
    rem=temp%10
    reverse=(reverse*10)+rem
    temp=temp//10
if n==reverse:
    print(n, 'is palindrome')
else:
    print('not a palindrome')
print('alternate method:')
reverse=int(str(n)[::-1])
if n==reverse:
    print(n,' is palindrome')
else:
    print(n,' not a palindrome')
