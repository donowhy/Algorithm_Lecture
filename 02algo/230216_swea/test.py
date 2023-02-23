# n, m = list(map(int, input().split()))
#
# s = []
#
#
# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, n + 1):
#         if i not in s:
#             s.append(i)
#             print(s, ' append')
#             dfs()
#             s.pop()
#             print(s, 'pop')
#
# dfs()
#
# #N과 M2
# N, M = map(int, input().split())
#
# numList = [i for i in range(0, N+1)]
# # [0, 1, 2, 3, 4]
#
# index = 0
#
# def backTracking(result):
#
#     # 개수에 맞게 꽉 찼다면 결과 출력
#     if len(result) == M:
#         print(*result)
#         return
#
#     for i in range(1, N+1):
#         # visited를 쓰면 더 짧게 걸릴 줄 알았는데,
#         # 왜 not in을 쓰면 더 짧게 걸릴까...
#         # 시간복잡도가 O(N)으로 알고 있는데 왜지...?
#         if (i not in result) and (len(result)==0 or i > result[-1]):
#             result.append(numList[i])
#             # 재귀로 백트래킹 실행
#             backTracking(result)
#             # 재귀 끝난 뒤 빠져나와서 바로 직전에 담았던 것 제거하기
#             result.pop()
#
# backTracking([])


# #수림 mountain
# T=int(input())
#
# for tc in range(1, T+1):
#     n=int(input())
#     dx=[-1,0,1,0,-1,-1,1,1] #위, 왼, 아래, 오, 왼위, 오위, 왼아래, 오아래
#     dy=[0,-1,0,1,-1,1,-1,1]
#     top=[]
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     for i in range(1,n):
#         for j in range(1,n):
#             for k in range(8):
#                 nx=i+dx[k] #8방 탐색
#                 ny=j+dy[k]
#                 print(nx, ny)
#                 if 0<=nx<n and 0<=ny<n:
#                     if arr[nx][ny] < arr[i][j]:
#                         if k!=7:
#                             continue
#                         else:
#                             top.append(arr[i][j])
#                     else:
#                         break
#     mx=-1
#     mn=301
#
#     if len(top) > 1:
#         for i in range(len(top)):
#             if top[i] < mn:
#                 mn = top[i]
#
#         for i in range(len(top)):
#             if top[i] > mx:
#                 mx = top[i]
#
#         print(f'#{tc} {mx-mn}')
#
#     else:
#         print(f'#{tc} -1')

#로봇
T = int(input())

for i in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    stk = [] #direction
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    x = y = 0

    while 0 <= x <= N and 0 <= y <= N and visited[x][y] is False:
        visited[x][y] = True
        stk.append(lst[x][y])
        nx = x + dx[lst[x][y]]
        ny = y + dy[lst[x][y]]
        x = nx
        y = ny

    print(f'#{i}',*stk)

# #로봇 함수 방법
# def dfs(visited, mapp, x, y):
#     global direction
#     if visited[x][y] == True:  # 기저조건
#         return
#     visited[x][y] = True  # 먼저 처음 시작하는 0,0은 방문처리
#
#     direction.append(mapp[x][y])  # 가능 방향 저장
#
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#
#     a= mapp[x][y]
#
#     nx= x+dx[a]
#     ny=y+dy[a]
#
#     if 0 <= nx < N and 0 <= ny < N:  # 이동하세요.
#         dfs(visited, mapp, nx, ny)  # 앞으로가자
#         return
#
#
# T = int(input())  # 구역의 개수, 테스트 케이스
# N = int(input())  # 행렬의 크기
#
# mapp = [list(map(int, input().split())) for _ in range(N)]
# direction = []
# visited = [[False] * N for i in range(N)]
# dfs(visited, mapp, 0, 0)
#
# print(f'#1', *direction)



# 고대 유적

# def count(arr):
#     mx = 2
#     for lst in arr:
#         cnt = 0
#         for n in lst:
#             if n == 1:
#                 cnt += 1
#                 if mx < cnt:
#                     mx = cnt
#             else:
#                 cnt = 0
#     return mx
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(M)]
#     arr_t = list(map(list, zip(*arr)))
#
#     ans = count(arr)
#     t = count(arr_t)
#     if ans < t:
#         ans = t
#     print(f'#{tc} {ans}')


#쇠막대기 자르기
# T = int(input())
#
# for tc in range(1, T+1):
#     st = input()
#     ans = cnt = 0
#     for i in range(len(st)):
#         if st[i] == '(':
#             cnt += 1
#         else:
#             if st[i-1] == '(': #레이저
#                 cnt -= 1
#                 ans += cnt
#             else: #막대기의 끝
#                 cnt -= 1
#                 ans += 1
#     print(f'#{tc} {ans}')

#arr 배열 안에 10 이하의 요소만 있는지 파악하는 코드
# arr = [1, 7, 3, 6, 9]

# #카운트 변수
# cnt = 0
# #arr 배열을 순회하면서 10미만의 요소가 있다면 cnt 1 증가.
# for i in arr:
#     if i < 10:
#         cnt += 1
#
# # cnt 변수와 arr 배열 크기가 같다면? (안의 모든 요소가 10 미만 값이다.)
# if cnt == len(arr):
#     print('모든 요소는 10 미만이에요!')
# else:
#     print('요소 중에 10이상인 값이 있어요!')


# def count(arr):
#     for i in arr:
#         if i > 10:
#             return False
#     return True
#
# if count(arr):
#     print('10미만')
# else:
#     print('10이상')


#for~ else문
#for문이 (break문이나 제어문에 의해 강제적으로 종료되지 않는 경우) 정상적으로 종료가 되면
#정상적으로 종료가 되면, else문의 코드 블럭을 실행합니다.
#
# for i in arr:
#     if i > 10:
#         break
# else:
#     print('10미만')
#
# print('코드 끝')


# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# arr[3:5] = [13, 15, 55, 66]
# print(arr)
#
# arr[3:] = 'hello'
# print(arr)
#
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# arr[5:5] =[10,10,10,10,10]
# print(arr)


#

