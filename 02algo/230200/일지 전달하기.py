N = int(input())

for i in range(1, N+1):
    num = int(input())
    for j in range(1, num+1):
        a, b = map(int,input().split())
        arr = [[1] * a for _ in range(b)]
    print(arr)


