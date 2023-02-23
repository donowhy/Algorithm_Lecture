# N = 8
# mazeArray = [[0, 0, 1, 1, 1, 1, 1, 1],
#              [1, 0, 0, 0, 0, 0, 0, 1],
#              [1, 1, 1, 0, 1, 1, 1, 1],
#              [1, 1, 1, 0, 1, 1, 1, 1],
#              [1, 0, 0, 0, 0, 0, 0, 1],
#              [1, 0, 1, 1, 1, 1, 1, 1],
#              [1, 0, 0, 0, 0, 0, 0, 0],
#              [1, 1, 1, 1, 1, 1, 1, 0]]
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# # visited : 방문 체크 배열
# visited = [[False] * N for _ in range(N)]
#
#
# # stack... <- 재귀호출로 최대한 처리 (시스템스택)
# # 현재 내가 가고 있는 방향, (x, y)
# def dfs(visited, x, y):
#     # (x, y) 좌표가 끝에 도달했을 때 탐색 성공! (기저조건)
#     if x == N - 1 and y == N - 1:
#         return True
#     # 내가 현재 있는 위치에 방문 체크
#     visited[x][y] = True
#     result = False
#     # 사방탐색을 해서 갈 수 있는 위치가 생기면
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 갈 수 있는 위치인지 체크 (갈 수 없는 위치에 있다면 탐색 다시 진행)
#         if nx < 0 and ny < 0 or nx >= N or ny >= N and mazeArray[nx][ny] == 1 or visited[nx][ny] == True:
#             continue
#
#         # 그 위치로 dfs함수를 재귀호출
#         result = dfs(visited, nx, ny)
#
#     return result
#
#
# result = dfs(visited, 0, 0)
# print(result)


# 방법 1

# def find_start(N, maze):
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 return 1 if DFS(i, j) else 0
#
#
# def DFS(x, y):
#     for i in range(4):  # 0, 1, 2, 3
#         nx = x + dx[i]
#         ny = y + dy[i]
#         print(nx, ny, 'nx, ny')
#         if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#             if not maze[nx][ny]:
#                 visited[nx][ny] = True
#                 if DFS(nx, ny):
#                     print(DFS(nx,ny), 'dfs(nx, ny)')
#                     return True
#             elif maze[nx][ny] == 3:
#                 return True
#
#
# T = int(input())
#
# for test in range(1, T + 1):
#     N = int(input())
#     maze = [list(map(int, list(input()))) for _ in range(N)]
#     visited = [[False] * N for _ in range(N)]
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     print(f'#{test} {int(find_start(N, maze))}')

# # 방법 2
# # 상하좌우 이동 리스트
# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#
# def boundary(y, x):  # 경계 체크
#     if y < 0 or x < 0 or y >= n or x >= n:
#         return True  # 경계 벗어남
#     return False
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     map_list = [list(map(int, list(input()))) for _ in range(n)]
#     y, x = 0, 0  # 시작좌표
#     result = 0  # 통로 연결되면 1로 바뀜
#     # 출발점(2) 찾기
#     for i in range(n):
#         if 2 in map_list[i]:
#             x = map_list[i].index(2)
#             y = i
#             break
#     stack = [(y, x)]  # 스택에 시작좌표 넣기
#     # 스택이 빌때까지 반복
#     while stack:
#         y, x = stack.pop()  # 현재 좌표 꺼내서
#         map_list[y][x] = 1  # 현재 좌표 방문처리
#         # 이동할 4방향 검사
#         for _y, _x in move:
#             dy = y + _y
#             dx = x + _x
#             # 경계 벗어나면 다음 길로
#             if boundary(dy, dx):
#                 continue
#             if map_list[dy][dx] == 3:  # 도착하면
#                 result = 1
#                 break  # 결과 바꾸고 반복문 종료
#             # 통로(0)를 만나면 스택에 추가
#             elif not map_list[dy][dx]:
#                 stack.append((dy, dx))
#         else:  # 브레이크 없이 끝나면 다음으로 진행
#             continue
#         break
#     print(f'#{tc} {result}')
#
# # 방법 3 DFS
# T = int(input())
#
#
# def isCondition(row, col):
#     return 0 <= row < N and 0 <= col < N and (row, col) not in visited and (grid[row][col] == 0 or grid[row][col] == 3)
#
#
# def dfs(row, col):
#     global res
#
#     if grid[row][col] == 3:
#         res = 1
#         return
#
#     dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
#
#     for dir in range(4):
#         nx = row + dx[dir]
#         ny = col + dy[dir]
#         if isCondition(nx, ny):
#             visited.append((nx, ny))
#             dfs(nx, ny)
#             visited.remove((nx, ny))
#
#
# for tc in range(T):
#
#     N = int(input())
#     grid = [list(map(int, input())) for _ in range(N)]
#     start_x = 0
#     start_y = 0
#     for i in range(N):
#         for j in range(N):
#             if grid[i][j] == 2:
#                 start_x, start_y = i, j
#                 break
#     res = 0
#     visited = []
#     dfs(start_x, start_y)
#     print("#{} {}".format(tc + 1, res))


#방법 4

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    N = int(input())
    maze = [0] * N
    for i in range(N):
        maze[i] = list(input())

    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                stack = []
                visited = [[0] * N for _ in range(N)]
                stack.append([i, j])
                visited[i][j] = True
                # print(stack, 'stack 첫번째')


                while stack:
                    x, y = stack.pop()
                    # print(x,y ,'x,y')

                    if maze[x][y] == '3':
                        result = 1
                        break

                    for t in range(4):
                        nx = x + dx[t]
                        ny = y + dy[t]

                        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] or maze[nx][ny] == '1':
                            continue

                        stack.append([nx, ny])
                        # print(stack, 'stack입니다.')
                        visited[nx][ny] = True

    print(f'#{test_case} {result}')
