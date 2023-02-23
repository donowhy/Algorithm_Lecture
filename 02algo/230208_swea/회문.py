
import sys

sys.stdin = open('input회문.txt', 'r')
import pprint

tc = int(input())

for test in range(tc):
    N, M = map(int, input().split())
    lst = []
    lstt = []
    for i in range(N):
        arr = list(input())
        lst.append(arr)
        # print(lst)
    for i in range(N):
        for j in range(N):
            lstt.append(lst[j][i])
            print(lstt)
            # for k in range(N):
            #
            #     garo = lst[i][j:k + 1]
            #     if garo == list(reversed(garo)) and garo != [] and len(garo) == M:
            #         print(lst[i][j:k+1])
            #
            #
            #     sero = lstt[i][j:k+1]
            #     if sero == list(reversed(sero)) and sero != [] and len(sero) == M:
            #         print(lstt[i][j:k+1])

    lsst=[]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                lstt
                lsst.append(lstt)
                print(lsst)


#방법
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    mapp1 = [input() for _ in range(N)]  # 제공된 단어맵
    mapp2 = [0 for _ in range(N)]  # 가로 <-> 세로

    for i in range(N):
        lines = []
        for j in range(N):
            lines += mapp1[j][i]
        line = ''.join(lines)
        mapp2[i] = line

    for i in range(N):
        w = h = ''
        for j in range(N):
            w = mapp1[i][j:j + M + 1]
            h = mapp2[i][j:j + M + 1]

            if w == w[::-1] and len(w) == M:
                print(f'#{tc}', w)

            elif h == h[::-1] and len(h) == M:
                print(f'#{tc}', h)

'''

1
5 5
GOFFA
OYECR
KWFSM
SLDLQ
ABCBA

'''
'''
JAEZN
'''