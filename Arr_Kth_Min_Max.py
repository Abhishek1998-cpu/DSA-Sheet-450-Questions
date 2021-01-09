# kth Smallest Element - GFG (kth Max and Min Element of the Array)
def kthSmallest(arr, l, r, k):
    arr.sort()
    return arr[k-1]


t = int(input())
for tcs in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    print(kthSmallest(arr, 0, n-1, k))
    # print("Hello")
