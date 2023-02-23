#
# def check(string):
#     global stack
#
#     for ch in string:
#         try:
#             if ch == '(':
#                 stack.append('(')
#             elif ch == ')':
#                 if stack.pop() == '(':
#                     continue
#                 return False
#             elif ch == '{':
#                 stack.append('{')
#             elif ch == '}':
#                 if stack.pop() == '{':
#                     continue
#                 return False
#
#         except:
#             return False
#
#     if len(stack) == 0:
#         return True
#     return False
#
#
#
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     stack = []
#     string = input().replace(' ','')
#     if check(string):
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')
#

# t = int(input())
# for tc in range(1, t + 1):
#     stack = []
#     n_lst = list(map(str, input()))
#     # print(n_lst,'list')
#     for ch in n_lst:
#         # print(ch, '반복')
#         if len(stack) == 0:
#             stack.append(ch)
#             # print(stack,'stack')
#         else:
#             if ch == stack[-1]:
#                 stack.pop()
#                 # print(stack,'stack')
#             else:
#                 stack.append(ch)
#                 # print(stack, 'stack')
#     print(f'#{tc} {len(stack)}')



# import sys
# sys.stdin = open('input.txt')
#
import pprint
#
# def dfs(start, end):
#
#     stack = []
#     visit = [False] * (V+1)
#     stack.append(start)
#     print(stack, 'staaaaaart')
#
#     while stack:
#         v = stack.pop()
#         print(v, 'pop')
#         visit[v]=True
#         for w in range(V+1):
#             if not visit[w]:
#                 if arr[v][w]:
#                     stack.append(w)
#                     print(stack, 'w')
#     return visit[end]
#
# T = int(input())
#
# for tc in range(1, T+1):
#     V, E = map(int,input().split())
#     arr = [[0] *(V+1) for _ in range(V+1)]
#     for _ in range(E):
#         x, y = map(int,input().split())
#         arr[x][y] = 1
#     # pprint.pprint(arr)
#     result = 1
#     a, b= map(int,input().split())
#     if not dfs(a,b):
#         result = 0
#     print(f'#{tc} {result}')
# #


# #1. 그래프 - 인접행렬로 작성하는 방법  (구현이 간단, 시간 복잡도가 증가)
# node, edge = map(int, input().split())  #노드와 간선의 수 (정점과 연결선 수)
#
# #노드의 갯수가 N, N*N 이차원 배열을 만든다.
# adj = [[0 for _ in range(node)] for _ in range(node)]
#
# #입력으로 노드간의 연결을 입력으로 받는다 ( 간선 정보)
# for _ in range(edge):
#     src, dest = map(int, input().split()) #시작정점과 끝정점을 입력받는다.
#     adj[src][dest] = 1 #src -> dest 연결점이 있을 때
#     adj[dest][src] = 1 #src <- dest 연결점이 있을 때  #서로 연결점이 있음
#
#
# # 2. 그래프 - 인접리스트로 작성하는 방법 (연결 관계만 기록, 조금 복잡, 연결관계를 2중 장부처럼 적기 때문에 메모리 손해를 볼 수 있음)
# # a -> b, c, f / b -> a, f...
#
# node, edge = map(int, input().split())  #노드와 간선의 수 (정점과 연결선 수)
#
# #노드의 갯수만큼 빈 리스트를 만든다.
# adj = [[] for _ in range(node)]
#
# for _ in range(edge):
#     src, dest = map(int, input().split())
#     adj[src].append(dest) #src -> dest 연결 정보를 추가
#     adj[dest].append(src) #src <- dest 연결 정보를 추가
#
#

# #방법 2
# def DFS(start, adj):
#     stack =[start, ]
#     v1 = []#방문해야되는곳
#     v2 = []#방문한곳
#     v1.append(start - 1)
#     while v1 :
#         node = v1.pop()
#         if not node in v2:
#             v2.append(node)
#             for idx, value in enumerate(adj[node]):
#                 if value == 1:
#                     v1.append(idx)
#     return v2
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     V, E = list(map(int, input().split()))
#     adj = [[0 for _ in range(V)] for _ in range(V)]
#     # 노드간의 연결을 입력으로 받는다
#     for _ in range(E):
#         S, G = map(int, input().split())
#         adj[S - 1][G - 1] = 1
#     start, end = map(int, input().split())
#     result = DFS(start, adj)
#     if end - 1 in result:
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')

#백만장자
tc = int(input())

for i in range(1, tc + 1):

    N = int(input())
    price = list(map(int,input().split()))
    # arr.append(price)
    hap = 0
    if price.index(max(price)) == 0:
        print(f'#{i} {hap}')

    while price:
        if price.index(max(price)) != 0:
            for j in range(price.index(max(price)),0,-1):
                max(price) - price[0]
                v = price.pop(0)
                hap += max(price) - v

                if price.index(max(price)) == 0:
                    price.pop(0)


        elif price.index(max(price)) == 0:
            price.pop(0)
    print(f'#{i} {hap}')

#방법 2
T = int(input())
for t in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    last = arr[-1]
    cnt = 0
    for i in range(len(arr)-1,-1,-1): # 핵심! 뒤부터 보기
        if last > arr[i]:
            cnt += last-arr[i]
        else: # 같거나 작을 때
            last = arr[i]
    print("#{} {}".format(t, cnt))