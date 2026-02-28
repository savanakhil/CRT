'''Time Complexity:
Defination: time complexity can be measure based upon the input 
                Ex:
                 n = 10
                 print(n)
                 
                 O(1)-->Constant time 
                 O(n)-->Single Loop
                 O(n^2)-->Two Loops
                 O(log n)-->Binary Search
                 O(n log n)-->Linearithmetic
                 O(2^n)-->Recursions'''
print("Time Complexity") #O(1)

# arr = [1,2,3,4,5] 
# for i in range(n):
#     print(i)       #O(n)
'''n = int(input())
arr = [1,2,3,4,5]
for i in range(n):
    for j in range(i+1, n)
    print(i,j)'''

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i 
#     return -1 
# print(linear_search([10,20,30,58,46],10))
# print(linear_search([10,20,30,58,46],46))
# print(linear_search([10,20,30,58,46],30))

def binary_search(arr, target):
    for i in range(len(arr -1)):
        if arr[i] == target:
            return i 
    return -1 
print(binary_search([10,20,30,58,46],10))
print(binary_search([10,20,30,58,46],46))
print(binary_search([10,20,30,58,46],30))