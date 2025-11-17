#sum of the first n natural numbers
n=int(input())
sum=0 
for i in range(n+1):
    sum=sum+i 
print(sum)
print('Alternate method:')
sum=int(n*(n+1)/2)
print(sum)
