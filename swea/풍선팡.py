'''
3
3 5
2 1 1 2 2
2 2 1 2 2
2 2 1 1 2
5 5
3 4 1 2 3
3 4 1 3 2
2 3 2 4 1
1 4 4 1 3
2 2 3 4 4
5 8
1 3 4 4 4 4 3 3
4 1 2 4 3 1 4 4
4 1 4 4 1 4 2 1
3 2 4 2 1 1 2 1
4 4 1 4 4 2 2 2
'''
import pprint

Tc = int(input())


for i in range(1, Tc + 1):
    N,M = map(int,input().split())
    lst = []
    arr = []

    for j in range(N):
        lst.append(list(map(int,input().split())))
    mx = 0
    for j in range(N):
        for l in range(M):
            if j-1 >= 0 and l-1 >= 0 and j+1 < N and l+1 < M:
                a = lst[j][l] + lst[j-1][l]+ lst[j][l-1] + lst[j+1][l] + lst[j][l+1]
                if mx < a:
                    mx = a
    print(mx)