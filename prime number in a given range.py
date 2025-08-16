import math
def checkprime(num):
    if num<2:
        return 0
    else:
        x=int(num/2)
        for i in range( 2,x+1):
            if num%i==0:
                return 0
        return 1
print('Enter lower and upper ranges:')
a=int(input())
b=int(input())
for i in range(a,b):
    if checkprime(i):
        print(i,end=' ')
