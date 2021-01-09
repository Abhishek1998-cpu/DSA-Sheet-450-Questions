def cyclic(Z):
    A = len(Z)
    B = Z[A-1]
    # print(B)
    for i in range(A-1, 0, -1):
        Z[i] = Z[i-1]
    Z[0] = B
    return Z

    # i = 0
    # temp = Z[i]
    # Z[i] = Z[i+1]
    # return Z


X = int(input())
for i in range(0, X):
    Y = int(input())
    Z = list(map(int, input().split(" ")))
    cyclic(Z)
    for i in range(0, len(Z)):
        print(Z[i], end=" ")


# Official Solution for This Problem GFG
# def rotate(arr, n):
#     x = arr[n - 1]

#     for i in range(n - 1, 0, -1):
#         arr[i] = arr[i - 1];

#     arr[0] = x;


# # Driver function
# arr= [1, 2, 3, 4, 5]
# n = len(arr)
# print ("Given array is")
# for i in range(0, n):
#     print (arr[i], end = ' ')

# rotate(arr, n)

# print ("\nRotated array is")
# for i in range(0, n):
#     print (arr[i], end = ' ')

# This solution is correct but having compilation problem of GFG platform
