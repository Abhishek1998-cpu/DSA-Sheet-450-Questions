# This is a solution of a problem Sort an array of 0s, 1s and 2s - GFG

# 1st Approach
# X = list(map(int, input().split(" ")))
# X.sort()
# print(X)

# 2nd Official Approach
def sort012(arr, n):
    arr.sort()
    return arr


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    sort012(arr, n)
    for i in arr:
        print(i, end=" ")
#     print()
# print("Hello World")

# arr = [int(x) for x in input().strip().split()]
# print(arr)
# for i in arr:
#     print(i, end=" ")
