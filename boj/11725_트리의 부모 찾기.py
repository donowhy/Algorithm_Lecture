# import sys
#
# T = int(sys.stdin.readline())
#
# # visited = [[False] for _ in range(T + 1)]
# arr = [[] for _ in range(T + 1)]
#
# for i in range(T-1):
#     N, M = map(int,input().split())
#     arr[N].append(M)
#     arr[M].append(N)
# print(arr)

# for i in range(1, T):


# #BFS
# import sys
# from collections import deque
#
# N = int(sys.stdin.readline())
# graph = [[] for i in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# queue = deque()
# queue.append(1)
#
# visited = [0]*(N+1)
#
# def bfs():
#     while queue:
#         now = queue.popleft()
#         for s in graph[now]:
#             if visited[s] == 0:
#                 visited[s] = now
#                 queue.append(s)
#
# bfs()
# res = visited[2:]
# for x in res:
#     print(x)


#
# #DFS
#
# import sys
# sys.setrecursionlimit(10**6)
# n = int(sys.stdin.readline())
#
# graph = [[] for i in range(n+1)]
#
# for i in range(n-1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [0]*(n+1)
# visited[1] = 1
#
# def dfs(s):
#     for i in graph[s]:
#         # print(i, 'i')
#         if visited[i] == 0:
#             visited[i] = s
#             # print(visited)
#             dfs(i)
#
# dfs(1)
#
# for x in range(2, n+1):
#     print(visited[x])


# #이진탐색
# def bi(num):
#     if num == node_tot:
#         return
#     for i in range(node_tot,2)
#
#
# for i in range(int(input())):
#     node_tot = int(input())
#     arr = [[] for _ in range(node_tot+1)]
#     arr[1].append(node_tot // 2 + 1)
#     print(arr)


# #방법 1
# T = int(input())
#
# def binary(i):
#     global cnt
#     if i <= N:
#         binary(2*i)
#         tree[i] = cnt
#         cnt += 1
#         binary(2*i+1)
#
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0 for _ in range(N+1)]
#
#     cnt = 1
#     binary(1)
#     print(f"#{tc} {tree[1]} {tree[N//2]}")


#
# #방법 2
# import sys
# sys.stdin = open("input.txt")
#
# T = int(input())
#
#
# def make_tree(n):
#     global number
#     # 배열이니까 배열크기 넘어가지 않도록
#     if n <= N:
#         # 왼쪽노드는 현재 인덱스의 2배
#         make_tree(n * 2)
#         # 더이상 못가면 값넣기
#         tree[n] = number
#         # 값 넣었으면 증가시키기
#         number += 1
#         # 우측 노드는 인덱스 2배 + 1
#         make_tree(n * 2 + 1)
#
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     tree = [0 for i in range(N + 1)]
#     number = 1
#     make_tree(1)
#     print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))


# from collections import deque
#
# def bfs(M):
#     dq.append(M)
#     while dq:
#         now = dq.popleft()
#         for s in arr[now]:
#             if cnt[s] == 0:
#                 dq.append(s)
#                 cnt[s] += 1
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int,input().split())
#     lst = list(map(int,input().split()))
#     arr = [[] for _ in range(N * 2)]
#
#     dq = deque()
#
#     for i in range(N):
#         arr[lst[i*2]].append(lst[i*2+1])
#
#     cnt = [0]*(N+2)
#     bfs(M)
#     print(sum(cnt)+1)



