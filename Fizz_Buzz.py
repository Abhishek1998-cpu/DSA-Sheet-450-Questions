# Fizz Buzz 
X = int(input())
for i in range(0, X):
    Y, Z = map(int, input().split(" "))
    for i in range(1, Y+1):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 5 == 0):
            print("Buzz")
        elif(i % 3 == 0):
            print("Fizz")
        else:
            print(i)
