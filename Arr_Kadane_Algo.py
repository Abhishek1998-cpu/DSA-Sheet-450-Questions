# Kadane's Algorithm -> Mostly used to find the largest Contiguous Subarray Sum -> GFG
# Sheet -> find largest sum contiguous Subarray
def Cont_arr(arr, size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here
        elif (max_ending_here < 0):
            max_ending_here = 0
        else:
            pass

    return max_so_far


X = list(map(int, input().split(" ")))
Y = len(X)
# print(X)
# print(Y)
print(Cont_arr(X, Y))


# Topic -> Arrays, Dynamic Programming
