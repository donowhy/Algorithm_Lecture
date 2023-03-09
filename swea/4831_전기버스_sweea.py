# T = int(input())
#
# for i in range(1,T+1):
#     cnt = 0
#     moved = 0
#     K, N, M = map(int, input().split())
#     stop = list(map(int, input().split()))
#     for j in range(M):
#         if moved < N:
#             # print(f'{moved} , {stop[j]}')
#             if moved == stop[j]:
#                 cnt += 1
#                 # print('딱도착', moved, stop[j])
#             elif moved > stop[j]:
#                 # print('지나감', moved, stop[j])
#                 moved = stop[j]
#                 cnt += 1
#
#
#         moved += K
#
#     for rng in range(1, M-1):
#         if stop[rng] - stop[rng-1] > K:
#             cnt = 0
#
#
#     print(f'#{i} {cnt}')

# 주유소를 먼저 찾는 방법
T = int(input())

for i in range(1, T + 1):
    cnt = 0
    moved = 0
    K, N, M = map(int, input().split())
    stop = list(map(int, input().split()))
    # print(f'K = {K}, N = {N}, M = {M}')
    # print(stop)

    for j in range(N):
        # back = 0 #안쓰는 변수
        # back_stop = 0
        print(f'현재 위치 = {moved} , 체크할 주유소 목록 = {stop}, 주유횟수 = {cnt}')
        if moved < N:  # 도착점 지나지 않았다면
            can = [moved+i for i in range(1, K+1)]  # 현재위치에서 이동가능한 좌표
            if N in can: # 이동 가능한 좌표중에 도착점이 있따면
                break
            print(can)
            can_list = list()
            for fuel_stop in stop:
                if fuel_stop in can:
                    print('주유가능')
                    can_list.append(fuel_stop)
            print(can_list)
            if can_list:
                moved = max(can_list)  # 주유가능한 목록중 가장 나중칸에서 주유
                cnt += 1
        else:
            # 도착점을 지났다면
            break

    for rng in range(1, M - 1): # 주유소 사이 거리가 갈수 없는 거리라면
        if stop[rng] - stop[rng - 1] > K:
            cnt = 0

    print(f'#{i} {cnt}')