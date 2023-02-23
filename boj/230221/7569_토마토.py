# # bfs 특 queue 사용하기
# # deque 모듈 안쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함)
# from collections import deque
#
# m, n, h = map(int, input().split())
# # 토마토 받아서 넣기. 이차원 리스트로 만들어질거.
# matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# print(matrix)
# # 좌표를 넣을거니까 []를 넣자.
# dq = deque([])
# # 방향 리스트. [dx[0], dy[0]]은 곧 [-1, 0]이고 이는 왼쪽으로 이동하는 위치이다.
# # 그려보면 이해하기 편함
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [0, 0, 0, 0, -1, 1]
# # 정답이 담길 변수
# result = 0
#
# # dq에 처음에 받은 토마토의 위치 좌표를 append 시킨다
# # n과 m을 사용하는걸 헷갈리지 말아야 함!
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if matrix[i][j][k] == 1:
#                 # print(i, j)
#                 dq.append([i, j, k])
#
#
# # bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
# def bfs():
#     while dq:
#         # 처음 토마토 좌표 x, y에 꺼내고
#         x, y, z = dq.popleft()
#         # print(x, y, z)
#         # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
#         for i in range(6):
#             nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z
#             # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
#             if 0 <= nx < n and 0 <= ny < m and 0<= nz < h and matrix[nx][ny][nz] == 0:
#                 # 익히고 1을 더해주면서 횟수를 세어주기
#                 # 여기서 나온 제일 큰 값이 정답이 될 것임
#                 matrix[nx][ny][nz] = matrix[x][y][z] + 1
#                 dq.append([nx, ny, nz])
#
#
# bfs()
#
# for i in matrix:
#     # print(i,'i')
#     for j in i:
#         for k in j:
#         # print(j, 'j')
#         # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
#             if k == 0:
#                 print(-1)
#                 exit(0)
#     # 다 익혔다면 최댓값이 정답
#     result = max(result, max(j))
# # 처음 시작을 1로 표현했으니 1을 빼준다.
# print(result - 1)
#
#
#
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# m, n, h = map(int, input().split())
#
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [0, 0, 0, 0, -1, 1]
#
# data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# queue = deque()
#
#
# # 3차원 bfs문제
# def bfs():
#     while queue:
#         # 높이, x,y 순서
#         z, x, y = queue.popleft()
#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]
#             if -1 < nx < n and -1 < ny < m and -1 < nz < h:
#                 # 높이, x,y 순서
#                 if data[nz][nx][ny] == 0:
#                     data[nz][nx][ny] = data[z][x][y] + 1
#                     queue.append((nz, nx, ny))
#
#
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             # 높이, x,y 순서
#             if data[i][j][k] == 1:
#                 # 높이, x,y 순서
#                 queue.append((i, j, k))
# bfs()
# flag = 0
# result = -2
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             # 높이, x,y 순서
#             if data[i][j][k] == 0:
#                 flag = 1
#                 # 높이, x,y 순서
#             result = max(result, data[i][j][k])
# if flag == 1:
#     print(-1)
# elif result == -1:
#     print(0)
# else:
#     print(result - 1)
# #



# import sys
# from collections import deque
#
# m, n, h = map(int, input().split())  # mn크기, h상자수
# graph = []
# queue = deque([])
#
# for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int, sys.stdin.readline().split())))
#         for k in range(m):
#             if tmp[j][k] == 1:
#                 queue.append([i, j, k])
#     graph.append(tmp)
#
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]
# while (queue):
#     x, y, z = queue.popleft()
#
#     for i in range(6):
#         a = x + dx[i]
#         b = y + dy[i]
#         c = z + dz[i]
#         if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
#             queue.append([a, b, c])
#             graph[a][b][c] = graph[x][y][z] + 1
#
# day = 0
# for i in graph:
#     for j in i:
#         for k in j:
#             if k == 0:
#                 print(-1)
#                 exit(0)
#         day = max(day, max(j))
# print(day - 1)
#
#
#
#
#
#
#
#
# import sys
# import collections
#
# input = sys.stdin.readline
# move = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]
# M, N, H = map(int, input().split())
# ripe = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# queue = collections.deque()
#
# # push all the ripe tomatoes into queue.
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if ripe[i][j][k] == 1:
#                 queue.append((i, j, k))
#
# # ripen the other tomatoes.
# while queue:  # bfs
#     i, j, k = queue.popleft()
#     for di, dj, dk in move:
#         ni, nj, nk = i + di, j + dj, k + dk
#         if ni < 0 or ni >= H or nj < 0 or nj >= N or nk < 0 or nk >= M:
#             continue
#         if ripe[ni][nj][nk] == -1:
#             continue
#         if not ripe[ni][nj][nk]:
#             ripe[ni][nj][nk] = ripe[i][j][k] + 1
#             queue.append((ni, nj, nk))
#
# # calculate the answer.
# answer = max(max(map(max, floor)) for floor in ripe) - 1
# for floor in ripe:
#     for row in floor:
#         if 0 in row:
#             answer = -1
# print(answer)



#
# for i in range(1,11):
#     a, b = map(int,input().split())
#
#     num_lst = [input().split()]
#
#
# def bfs(start):
#     queue = []
#     visited = [False for _ in range(len(num_lst))]
#     queue.append(start)
#     visited[start] = True
#
#     while queue:
#         node = queue.pop(0)




#
# from _collections import deque
#
# def contact(current_q):
#     global result
#     # 마지막 연락받은 사람들 중 가장 큰 값
#     result = max(current_q)
#
#     # 다음 연락 받을 사람들이 들어갈 리스트
#     next_q = deque()
#
#     # 현재 연락받은 사람들이 연락 할 사람들을 찾는 과정
#     while current_q:
#         # print(current_q, '현재 큐')
#         c = current_q.pop()
#         for neighbor in adj[c]:
#             if visited[neighbor] == False:
#                 next_q.append(neighbor)
#                 # print(next_q)
#                 visited[neighbor] = True
#
#     # 만약 다음에 연락 받을 사람이 있으면
#     if next_q:
#         contact(next_q)
#
#
# for tc in range(1, 2):
#     n, start = map(int, input().split())
#     # 인접 리스트를 만든다
#     adj_list = list(map(int, input().split()))
#     adj = {i: [] for i in range(1, 101)}
#
#     for i in range(0, n, 2):
#         adj[adj_list[i]].append(adj_list[i + 1])
#     # 방문 체크 리스트, 결과 값 저장, q
#     visited = [False] * 101
#     visited[start] = True
#     result = 0
#     q = deque()
#     q.append(start)
#
#     contact(q)
#     print(f'#{tc} {result}')





#
# def bfs(s):    #bfs 함수 만들기
#     queue = [s]  #큐에 시작하는 값 넣기
#     visited[s] = True  #시작하는 값을 True로 표시
#     while queue:
#         x = queue.pop(0)
#         # print(x,'엑스')
#         for i in graph[x]:
#             print(visited[x], 'visited[x]')
#             if visited[i] == False:
#                 visited[i] = visited[x] + 1
#                 # print(visited,visited[i], '비짓 i')
#                 queue.append(i)
#
#
# T = 1
# for tc in range(1, T + 1):
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#     visited = [False] * 101
#     graph = [[] for _ in range(101)]
#
#     for i in range(0, N, 2):
#         graph[arr[i]].append(arr[i + 1])
#
#     bfs(S)
#     a = max(visited)
#     max_n = 0
#     for i in range(len(graph)):
#         if visited[i] == a and max_n < i:
#             max_n = i
#     print(f'#{tc} {max_n}')


