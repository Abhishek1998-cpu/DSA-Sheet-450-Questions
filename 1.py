class Solution:
    def merge(self, arr1, arr2, n, m):
        self.arr1 = arr1
        self.arr2 = arr2
        self.n = n
        self.m = m
        int(n)
        int(m)
        for i in range(0, len(arr2)):
            arr1.append(arr2[i])
        arr1.sort()
        # arr1 = arr1[0: n-1]
        # arr2 = arr2[n-1: m-1]
        # return arr1 and arr2
        return len(arr1)


tc = int(input())
while tc > 0:
    n, m = map(int, input().split(" "))
    # print(n)
    # print(m)
    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))
    ob = Solution()
    ans = ob.merge(arr1, arr2, n, m)
    # for x in arr1:
    #     print(x, end=" ")
    # print()
    # for x in arr2:
    #     print(x, end=" ")
    print()
    print(ob.merge(arr1, arr2, n, m))
    tc = tc - 1
