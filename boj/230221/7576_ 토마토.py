# # bfs 특 queue 사용하기
# # deque 모듈 안쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(n)이고 popleft()가 O(1)이라고 함)
# from collections import deque
#
# m, n = map(int, input().split())
# # 토마토 받아서 넣기. 이차원 리스트로 만들어질거.
# matrix = [list(map(int, input().split())) for _ in range(n)]
# # 좌표를 넣을거니까 []를 넣자.
# dq= deque([])
# # 방향 리스트. [dx[0], dy[0]]은 곧 [-1, 0]이고 이는 왼쪽으로 이동하는 위치이다.
# # 그려보면 이해하기 편함
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# # 정답이 담길 변수
# result = 0
#
# # dq에 처음에 받은 토마토의 위치 좌표를 append 시킨다
# # n과 m을 사용하는걸 헷갈리지 말아야 함!
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == 1:
#             # print(i, j)
#             dq.append([i, j])
#
# # bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
# def bfs():
#     while dq:
#         # 처음 토마토 좌표 x, y에 꺼내고
#         x, y = dq.popleft()
#         # print(x, y)
#         # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
#         for i in range(4):
#             nx, ny = dx[i] + x, dy[i] + y
#             # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
#             if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
#                 # 익히고 1을 더해주면서 횟수를 세어주기
#                 # 여기서 나온 제일 큰 값이 정답이 될 것임
#                 matrix[nx][ny] = matrix[x][y] + 1
#                 dq.append([nx, ny])
#
# bfs()
#
# for i in matrix:
#     # print(i,'i')
#     for j in i:
#         # print(j, 'j')
#         # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
#         if j == 0:
#             print(-1)
#             exit(0)
#     # 다 익혔다면 최댓값이 정답
#     result = max(result, max(i))
# # 처음 시작을 1로 표현했으니 1을 빼준다.
# print(result - 1)


# from collections import deque
# #
# def bfs():
#     while dq:
#         x, y = dq.popleft()
#         for i in range(4):
#             nx, ny = dx[i] + x ,  dy[i] + y
#             if 0<= nx < N and 0 <= ny < N and matrix[nx][ny] == '0':
#                 matrix[nx][ny] = matrix[x][y] + 1
#                 dq.append([nx, ny])
#
#             elif 0<= nx < N and 0 <= ny < N and matrix[nx][ny] == '3':
#                 matrix[nx][ny] = matrix[x][y] + 1
#                 dq.append([nx, ny])
#
#
# T = int(input())
#
# for i in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int,input())) for _ in range(N)]
#     visited = [[False] * N for _ in range(N)]
#     dq = deque()
#
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     res = 0
#
#     for j in range(N):
#         for k in range(N):
#             # print(matrix[i][j])
#             if matrix[j][k] == '2':
#                 print(j, k)
#                 dq.append([j,k])
#
#     bfs()
#
#     for j in matrix:
#         res = max(res, max(j))
#     print(res - 1)

#
# from collections import deque
#
# def bfs(x, y):
#     q = (x, y)
#     visited = [[False]*(N+1) for _ in range(N+1)]
#     deq = deque()
#     deq.append(q)
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     visited[x][y] = 1
#     while deq:
#         i, j = deq.popleft()
#         if data[i][j] == 3:
#             return visited[i][j]
#
#         for k in range(4):
#             nx = dx[k] + i
#             ny = dy[k] + j
#
#             if not(0 <= nx < N and 0 <= ny < N):
#                 continue
#             if (data[nx][ny] == 0 or data[nx][ny] == 3) and visited[nx][ny] == 0:
#                 deq.append((nx, ny))
#                 visited[nx][ny] = visited[i][j] + 1
#
#     return 2
#
# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     data = [list(map(int, input())) for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if data[i][j] == 2:
#                 res = bfs(i, j) - 2
#     print(f'#{tc} {res}')

#
# TC = int(input())
# for tc in range(1, TC+1):
#     V, E = map(int,input().split())
#     data = [list(map(int, input().split())) for _ in range(V)]
#     # print(data)
#     graph = [[] for _ in range(1001)]
#
#     for i in range(V):
#         graph[data[i][0]].append(data[i][1])
#     # print(graph)
#
# def bfs(s):
#     queue = [s]
#     visited[s] = True


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
#
# from collections import deque
#
# T = int(input())
# # BFS: start 노드를 시작해서-> end 노드에 도착할 때 까지
# # 다음 노드로 건너갈 때 마다 카운트 1 씩..
# def bfs(start, end):
#     #방문체크를 하기 위해 배열
#     visited = [False for _ in range(V+1)]
#
#     dq = deque
#     dq.append(start) #첫 시작 정점을 넣어준다.
#     visited[start] = True
#     results = [0 for _ in range(V+1)]
#     results[start] = 0
#
#     while dq: #큐가 빌 때까지 반복하겠다.
#         node = dq.popleft()
#         #해당 노드에서 다른 인접한 노드로 건너갈 수 있는 것들을 탐색.
#         for nxt_node in adj[node]:
#             #방문 체크를 먼저 해줘야한다.
#             if visited[nxt_node] == False:
#                 dq.append(nxt_node)
#                 visited[nxt_node] = True
#                 results[nxt_node] = results[node] + 1 #이전 노드 간선에서 +1만큼
#     #BFS 탐색이 종료된 것이기 때문에
#     return results[end]
#
# for tc in range(1 , T + 1):
#     V, E = map(int,input().split())
#     #인접 리스트 : a 정점 노드에서 연결되어 있는 노드들을 리스트에 넣는 것
#     # a : 1 -> [2,3,5]
#     adj = [[] for _ in range(V+1)]
#     for _ in range(E):
#         a, b = map(int,input().split())
#         adj[a].append(b) # a -> b
#         adj[b].append(a) # b -> a
#     S, G = map(int,input().split())
#
#     #BFS 탐색해서 S -> ..-> G의 간선 갯수를 출력
#     res = bfs(S,G)
#     print(f'#{tc} {res}')


# BFS 함수
#
# def bfs(queue):
#     count = 1
#     # 큐가 빌때까지 반복
#
#     while queue:
#         # 2개의 큐가 필요하므로 한개더 생성한다.
#         s_queue = []
#         # 큐가 빌때까지 반복한다.
#         while queue:
#             # 원소를 꺼내서
#             index = queue.pop()
#             # 연결되어 있는 부분들을 확인한다.
#             for i in node[index]:
#                 # 이미 방문했다면 넘어간다.
#                 if visited[i]:
#                     continue
#                 # 도착지와 일치한다면 이동거리를 반환한다.
#                 if i == end:
#                     return count
#                 # 위의 조건에 걸리지 않는다면 두번재 큐에 추가한다.
#                 s_queue.append(i)
#                 # 방문처리를 한다.
#                 visited[i] = 1
#         # 모든 큐가 비었다면 카운트를 증가시킨다.
#         count += 1
#         # 큐를 교체한다.
#         queue = s_queue
#     # 여기까지 왔다면 목적지까지 도착할 수 없다.
#     return 0
#
#
# for t in range(1, int(input()) + 1):
#     # V개의 노드, E개의 간선
#     V, E = map(int, input().split())
#     # 리스트를 이용한 간선 표시
#     node = [[] for _ in range(V + 1)]
#     # 방문여부
#     visited = [0 for _ in range(V + 1)]
#     # 데이터 편집
#     for i in range(E):
#         a, b = map(int, input().split())
#         node[a].append(b)
#         node[b].append(a)
#     # 시작노드와 끝나는 노드 저장
#     start, end = map(int, input().split())
#     # 시작노드 방문처리
#     visited[start] = 1
#     # bfs 돌리기
#     print(f'#{t} {bfs([start])}')

from collections import deque
dq = deque

a, b = map(int,input().split())
lst = list(map(int,input().split()))
arr = list(map(int,input().split()))
cnt = 1
hap = 0
board = []
while True:
    for i in range(len(arr)):
        print(i)
        # board.append(sum(arr[i]))
        # if board > lst[0]:
        #     arr.popleft() * (i-1)
        #     lst.popleft()
        #     cnt += 1
        #     if sum(arr) < lst[0]:
        break




d, n = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))

for i in range(1, len(oven)):  # 이분탐색 적용을 위해 적절히 변경
    if oven[i] > oven[i - 1]:
        oven[i] = oven[i - 1]

piled_loc = 0  # 도우가 어디 쌓이는지
lp, rp = 0, len(oven) - 1
for dough in doughs:
    is_piled = False  # False로 남으면 도우를 더 못쌓는다는 뜻

    while lp <= rp:
        mid = (lp + rp) // 2
        diameter = oven[mid]
        if diameter >= dough:
            lp = mid + 1
            piled_loc = mid
            is_piled = True
        else:
            rp = mid - 1

    if not is_piled:
        piled_loc = -1
        break

    lp = 0
    rp = piled_loc - 1  # 도우가 쌓이면 rp값 갱신

if piled_loc == -1:
    print(0)
else:
    print(piled_loc + 1)





