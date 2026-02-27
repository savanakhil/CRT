# li = [1,2,3,4,5]
# ans = []
# for i in li:
#     ans.append(i**2)
# print(ans)
'''Intermediate patterns'''
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)
'''Diamond'''
# n = int(input())
# for i in range (1,n+1):
#     print(" "*(n-i)+"* "*i)
# for i in range(n,0,-1):
#     print(" "*(n-i)+"* "*i)

# n = int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()
'''or'''
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+" ".join([str(j) for k in range(1,i+1)])) 
#     n = 4
# output: 
#    1
#   1 2
#  1 2 3
# 1 2 3 4

# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+" ".join([str(i)for k in range(1,i+1)]))

#     n=4
# output:
#    1
#   2 2
#  3 3 3
# 4 4 4 4