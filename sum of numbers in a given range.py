# sum of the natural numbers in a given range
print('First method:')
a=int(input('enter a value:'))
b=int(input('enter value:'))
sum=0
for i in range(a,b+1):
    sum=sum+i
print(sum)
print('time complexity is O(n)')
print('space complexity is O(1)')
print('alternate method:')
sum=int((b*(b+1)/2)-(a*(a+1)/2))+a 
print("sum is",sum)
print('time complexity : O(1)')
print('space complexity :O(1)')
