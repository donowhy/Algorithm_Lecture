import pprint
# 1 1 5 6 10 10 20 30
for _ in range(1):
    lst = list(map(int,input().split()))
    arr = [[0]*max(lst) for _ in range(max(lst))]
    # arr_a =[[0]* 30 for _ in range(30)]
    for i in range(lst[0],lst[2]):
        for j in range(lst[1],lst[3]):
            arr[i][j] += 1

    for k in range(lst[4], lst[6]):
        for l in range(lst[5], lst[7]):
            arr[k][l] += 1

    cnt = 0
    for m in range(max(lst)):
        for n in range(max(lst)):
            if arr[m][l] == 1:
                cnt += 1
                cnt == (((lst[2]-lst[0]) * lst[3]-lst[1]) + ((lst[6]-lst[4]) * (lst[7]-lst[5])))
        print('d')

            if arr[m][l] == 2:
                cnt += 1
        if cnt == 1:
            print('c')


#방법 1
import sys
input = sys.stdin.readline

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue
    elif x1==p2 or x2==p1:
        if q1==y2 or q2==y1:
            print('c')
            continue
        else:
            print('b')
            continue
    elif q1==y2 or q2==y1:
            print('b')
            continue
    else:
        print('a')
        continue

#방법 2
for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    #// 1번과정
    xl = max(x1, x2)
    xr = min(p1, p2)
    yb = max(y1, y2)
    yt = min(q1, q2)

    #// 2번과정
    xdiff = xr - xl
    ydiff = yt - yb

    #// 3번과정
    if xdiff > 0 and ydiff > 0:
        print('a')
    elif xdiff < 0 or ydiff < 0:
        print('d')
    elif xdiff == 0 and ydiff == 0:
        print('c')
    else:
        print('b')


#방법 3
import sys


input = sys.stdin.readline

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # case (d)
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue

    elif x1 == p2 or x2 == p1:
        # case (c)
        if q1 == y2 or q2 == y1:
            print('c')
            continue
            # case (b)
            else:
            print('b')
            continue
    elif q1 == y2 or q2 == y1:
        print('b')
        continue

    # case (a)
    else:
        print('a')
        continue