'''Square pattern'''
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*")
#     print()
'''Lower Triangle'''
# n = int(input())
# for i in range(n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
'''Upper Triangle'''
# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
'''Number series'''
# n = int(input())
# num=1
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()

# k = 65
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(chr(k+j),end=" ")
#         k+=1
#     print()

n = int(input())
for i in range(n+1):
    for j in range(n+1):
        if (i==0 or i==n or j==0 or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()