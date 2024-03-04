n=int(input())
sum=0 
for i in range(n+1):
    sum=sum+i 
print(sum)
print('alternate method:')
sum=int(n*(n+1)/2)
print(sum)