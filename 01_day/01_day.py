# # 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# #
# # 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# #
# # 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 100 )
# #로직을 처리하고
# # 9 <- N
# # 7 4 2 0 0 6 0 7 0 <- arr
# #가장 큰 카운트 값을 가지는 변수
# mxcnt = 0
# #      //       리스트의 인덱스를 저장하는 것도 필요
# mxidx = 0
# #카운트 변수
# cnt = 0
# #arr 리스트에서 인덱스 순회 i:0 -> N-1
#     #arr j: i + 1 -> N -1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#
# for i in range(N):
#     for j in range(i+1, N):
#         if arr[i] > arr[j]: #카운트 1증가
#             cnt += 1
#
#     if mxcnt < cnt: #인덱스 갱신
#         mxcnt = cnt
#         mxidx = i
#
#     cnt = 0
#
#
# print(f'#{tc} {mxcnt}')


# #min max

#
# T = int(input())
# for i in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     mx = 0
#     mn = arr[0]
#     for j in range(N):
#         if mx < arr[j]:
#             mx = arr[j]
#     for k in range(N):
#         if mn >= arr[k]:
#             mn = arr[k]
#
#     print(f'#{i+ 1} {mx-mn}')


# 구간 합

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_arr = []

    mx = 0
    mn = 0

    for j in range(M):
        mx += arr[j]
        mn += arr[j]

    for k in range(N-M+1):
        s = 0
        for l in range(k, M+k):
            s += arr[l]

        if s > mx:
            mx = s
        if s < mn:
            mn = s

    print(f'#{i+1} {mx-mn}')

#
# T = int(input())
# for i in range(T):
#     N, M = map(int,input().split())
#     arr = list(map(int, input().split()))
#     for i in range(N - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     print(*arr)
