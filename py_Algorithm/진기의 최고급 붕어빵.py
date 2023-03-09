for t in range(int(input())):
    N, M, K = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    tree = [0] * 11112

    for i in range(M,11112):
        tree[i] = i//M * K

    j = 1
    res = 0
    for i in lst:
        if tree[i] - j >= 0:
            res += 1

        j += 1


    if res == N:
        print(f'#{t+1} Possible')
    else:
        print(f'#{t+1} Impossible')


'''
6
2 2 2
3 4
2 2 2
1 2
10 2 1
4 20 8 10 16 14 18 12 6 2
5 2 1
3 2 2 2 5 
2 2 1
4 2
2 2 1
3 2
'''
