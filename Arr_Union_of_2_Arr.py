# Union of two Arrays - GFG

A = int(input())
for i in range(0, A):
    B = list(map(int, input().split(" ")))
    C = list(map(int, input().split(" ")))
    D = list(map(int, input().split(" ")))
    E = C + D
    E = set(E)
    E = list(E)
    F = len(E)
    print(F)
    # print("Hello")
