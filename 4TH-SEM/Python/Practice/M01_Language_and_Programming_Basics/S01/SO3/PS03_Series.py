# Display Arithmetic Progression values upto 10
# a = int(input())
# d = int(input())
# n = 10
# for i in range(n):
#     c=a+i*d
#     print(c,end=",")

'''(Fibonacci series)a = 0
b = 1 
n = int(input())
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b'''
  '''OR'''

#fibonacci
# n = int(input())
# fii = [0,1]
# for i in range(2,n):
#     fii.append(fii[i-2] + fii[i-1])
# print(fii)




#Armstrong number
# n = int(input())
# l = len(str(n))
# res = 0
# for i in str(n):
#     res+=int(i)**l 
# print("Armstrong" if n == res else "not Armstrong")

'''Perfect/Not Perfect number
n = int(input())
sum = 0
for i in range(1,n):
    if n%i==0:
        sum += i
print("Perfect" if sum == n else "Not Perfect")'''


def factorial(n):
    if n<0:
        return "No Factorial for -ve"
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact*=i 
        return fact 
s=0
n=int(input())
for i in range(n):
    s += factorial(int(i))
print("Strong number" )