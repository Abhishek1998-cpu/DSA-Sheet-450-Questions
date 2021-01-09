class Solution:
    def getMinDiff(self, arr, n, k):
        self.arr = arr
        self.n = n
        self.k = k
        # A = []
        A = sorted(arr)  # We will use sorted here
        # print(A)
        # print(arr)
        ans = A[n-1] - A[0]
        small = A[0] + k
        big = A[n-1] - k
        for i in range(1, len(arr)-1):
            Sub = arr[i] - k
            add = arr[i] + k
            if (Sub >= small or add <= big):
                continue

        # Either subtraction causes a smaller
        # number or addition causes a greater
        # number. Update small or big using
        # greedy approach (If big - subtract
        # causes smaller diff, update small
        # Else update big)
            if (big - Sub <= add - small):
                small = Sub
            else:
                big = add

        return min(ans, big - small)

    #     print(arr[i], end=" ")
    # return


K = int(input())
N = int(input())
X = list(map(int, input().split(" ")))
Y = Solution()
# Z = Y.getMinDiff(X, N, K)
print(Y.getMinDiff(X, N, K))


# https://realpython.com/python-sort/
