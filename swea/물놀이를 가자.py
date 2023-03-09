# # from collections import deque
# #
# # # dx = [1, -1, 0, 0]
# # # dy = [0, 0, 1, -1]
# #
# #
# # def cal():
# #     global cnt
# #
# #     while dq:
# #         lst = []
# #         x, y = dq.popleft()
# #         for i in water:
# #             lst.append(abs(x-i[0]) + abs(y-i[1]))
# #         ans.append(min(lst))
# #
# #
# # for t in range(int(input())):
# #     N, M = map(int, input().split())
# #     board = [list(input()) for _ in range(N)]
# #     dq = deque()
# #     water = deque()
# #     ans = []
# #
# #     for i in range(N):
# #         for j in range(M):
# #             if board[i][j] == 'L':
# #                 # print(i, j)
# #                 dq.append([i, j])
# #             if board[i][j] == 'W':
# #                 water.append([i,j])
# #
# #     cal()
# #     print(f'#{t} {sum(ans)}')
#
# #
# from collections import deque
#
# def cal():
#     while land:
#         lst = set()
#         x, y = land.popleft()
#         for i in water:
#             lst.add(abs(x-i[0]) + abs(y-i[1]))
#             # print(lst)
#         ans.append(min(lst))
#
#
# for t in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     board = [list(input()) for _ in range(N)]
#     land = deque()
#     water = deque()
#     ans = []
#
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 'L':
#                 land.append([i, j])
#             if board[i][j] == 'W':
#                 water.append([i,j])
#
#     cal()
#     print(f'#{t} {sum(ans)}')
#
#
# #
# # def bfs():
# #
# #     dx = [-1, 1, 0, 0]
# #     dy = [0, 0, -1, 1]
# #     for i in range(N):
# #         for j in range(M):
# #             if board[i][j] == 'L':
# #                 dq.append([i, j])
# #                 visited = [[0] * M for _ in range(N)]
# #
# #                 while dq:
# #                     x, y = dq.popleft()
# #                     print(x, y, 'x, y')
# #                     for k in range(4):
# #                         nx = x + dx[k]
# #                         ny = y + dy[k]
# #
# #                         if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or visited[nx][ny]:
# #                             continue
# #                         else:
# #                             print(nx, ny, 'nx, ny')
# #                         if board[nx][ny] == 'W':
# #                             visited[x][y] += 1
# #                             res.append(min(visited))
# #                             break
# #                         else:
# #                             dq.append([nx, ny])
# #                             visited[nx][ny] = visited[x][y] + 1
# #                             print(visited)
# #
# #
# #
# #
# # from collections import deque
# #
# # for test_case in range(1, int(input()) + 1):
# #     N, M = map(int, input().split())
# #     board = [list(input()) for _ in range(N)]
# #
# #     dq = deque()
# #     res =[]
# #
# #     bfs()
# #
# #     print(f'#{test_case} {res}')
#
#
#


from collections import deque


def check():
    global cnt
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    while save:
        y, x, cnt = save.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= N or nx >= M or mark[ny][nx] != -1:
                continue
            save.append((ny, nx, cnt + 1))
            mark[ny][nx] = cnt + 1


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    land = [input() for _ in range(N)]
    mark = [[-1] * M for _ in range(N)]
    save = deque()
    cnt = 0

    for y in range(N):
        for x in range(M):
            if land[y][x] == 'W':
                save.append((y, x, 0))
                mark[y][x] = 0

    check()

    mx = 0
    for i in mark:
        mx += sum(i)
    print(f'#{t} {mx}')