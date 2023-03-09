# import sys
# input = sys.stdin.readline
#
# while True:
#     N, M = map(int,input().split())
#     if N == M == 0:
#         break
#     dq = {}
#
#     lst = [list(input().split()) for _ in range(M)]
#
#     for i in range(M):
#         if lst[i][0] == '!':
#             if dq.get(lst[i][1]) == None and dq.get(lst[i][2]) == None:
#                 dq[lst[i][1]] = 0
#                 dq[lst[i][2]] = int(lst[i][3])
#
#             elif dq.get(lst[i][1]) == None and dq.get(lst[i][2]) != None:
#                 dq[lst[i][1]] = int(dq.get(lst[i][2])) - int(lst[i][3])
#
#             elif dq.get(lst[i][1]) != None and dq.get(lst[i][2]) == None:
#                 dq[lst[i][2]] = int(dq.get(lst[i][1])) + int(lst[i][3])
#             else:
#                 if int(dq.get(lst[i][2])) - int(dq.get(lst[i][1])) == lst[i][3]:
#                     continue
#
#
#         elif lst[i][0] == '?':
#             try:
#                 print(int(dq.get(lst[i][2])) - int(dq.get(lst[i][1])))
#             except:
#                 print('UNKNOWN')
#     print(dq, len(dq))
# import pprint
#

for t in range(1, 11):
    T = int(input())
    arr = [[] for _ in range(100)]
    lst = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if lst[j][i] == 2:
                arr[i].append(2)
            if lst[j][i] == 1:
                arr[i].append(1)
    cnt = 0

    for i in range(100):
        for j in range(len(arr[i]) - 1):
            if arr[i][j] == 1 and arr[i][j] != arr[i][j+1]:
                cnt += 1
    print(f'#{t} {cnt}')




