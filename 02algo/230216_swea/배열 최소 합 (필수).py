# A = [1, 2, 3]
#
# def f(i,N):
#     # 기저조건 (i == N) 종료해
#     if i == N: #순열완성
#         print(A)
#         return
#
#     # for j : i -> N-1 [i,N)
#     for j in range(i, N):
#         #배열 요소 교환
#         A[i], A[j] = A[j], A[i]
#         f(i+1, N)
#         #배열 요소 원복
#         A[i], A[j] = A[j], A[i]
#
# A = [1,2,3]
# N = len(A)
# f(0,N)
#
#
# # row를 파라미터로 받는 최소 합을 찾는 함수
# def find_min(row):
#     global partial_sum, min_sum
#     # pruning을 위한 조건
#     # 부분합이 이미 최소합보다 크게되면 더 내려갈 의미가 없다.
#     if partial_sum > min_sum:
#         return
#     # 마지막 행에 도달하면 종료한다.
#     # 아직 더하는 연산이 없으므로 조건은 N-1이 아니라 N이 되어야한다.
#     if row == N:
#         # 마지막에 도달했는데 부분합이 최소합보다 작다면 갱신해준다.
#         if partial_sum < min_sum:
#             min_sum = partial_sum
#     # i는 col를 의미한다
#     for i in range(N):
#         # 아직 방문하지 않은 col이라면
#         if not visited[i]:
#             # 특정 row의 i번째 값으로 결정이 되있을 때에
#             # 방문으로 갱신
#             visited[i] = True
#             partial_sum += arry[row][i]
#             # i로 결정했을 때 그 아래를 계산한다.
#             find_min(row + 1)
#             # find_min이 바닥까지 가거나 pruning 된 후에야 위에 것이 끝나므로
#             # 다시 현재 row로 올라와야 한다.
#             visited[i] = False
#             partial_sum -= arry[row][i]
#
#
# # 테스트케이스 입력
# T = int(input())
# for idx in range(T):
#     # 배열의 길이
#     N = int(input())
#     arry = [list(map(int, input().split())) for _ in range(N)]
#     # 방문한 배열의 col 번호를 저장하기 위한 배열
#     visited = [False] * N
#     # 부분합과 최소값을 저장할 변수
#     # (N이 10보다 작고 10보다 작은 자연수가 주어지므로 최소값의 시작은 1000이면 충분)
#     partial_sum, min_sum = 0, 1000
#     # 최소 값을 찾기위한 함수
#     find_min(0)
#     print(min_sum)
#
#
#
# #방법 2
# def section_sum(idx, total):
#     global answer
#
#     if idx == N:
#         if total < answer:
#             answer = total
#             return
#
#     if total > answer:
#         return
#
#     for i in range(N):
#         if i not in visited:
#             visited.append(i)
#             section_sum(idx+1, total+matrix[idx][i])
#             visited.pop()
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     answer = 30
#     visited = []
#     section_sum(0, 0)
#     print('#{} {}'.format(tc, answer))
#
#
# #방법 3
# def backtracking(i, N, s, visited):
#     global sumV
#     if i == N:
#         if s < sumV:
#             sumV = s
#     elif s > sumV:
#         return
#     else:
#         for j in range(N):
#             if not visited[j]:
#                 visited[j] = 1
#                 backtracking(i+1, N, s+num_list[i][j], visited)
#                 visited[j] = 0
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     num_list = [list(map(int, input().split())) for _ in range(N)]
#     sumV = 100
#     visited = [0]*N
#
#     backtracking(0, N, 0, visited)
#     print(f'#{tc + 1} {sumV}')

#
# def count(idx, visited, SUM):
#     global MIN
#     if idx >= N:
#         if SUM < MIN:
#             MIN = SUM
#         return
#
#     if SUM > MIN:
#         return
#     for k in range(0, N):
#         if visited[k] == 0:  # k번째 값에 접근한 적이 없다면
#             SUM += maze[idx][k]
#             # print(SUM, 'sum+= maze')
#             visited[k] = 1
#             count(idx + 1, visited, SUM)
#             visited[k] = 0  # 원상복구
#             SUM -= maze[idx][k]
#             # print(SUM, 'sum -= maze')
#
#
# T = int(input())
# for TC in range(1, T + 1):
#     N = int(input())
#     maze = []
#     for i in range(N):
#         arr = list(map(int, input().split()))
#         maze.append(arr)
#         # print(maze)
#
#     visited = {}
#     for i in range(0, N):
#         visited[i] = 0
#     SUM = 0
#     MIN = 99999
#
#     count(0, visited, SUM)
#
#     print("#%d %d" % (TC, MIN))





def divide_two(start, end):
    if start == end:
        return start  # 한명 남았다는 의미이므로 가위바위보를 위해 리턴

    a = divide_two(start, (start +end) // 2) #idx 값으로 반환
    b = divide_two((start + end) // 2 + 1, end)
    print(a, b) # idx 값
    return rsp(a, b)  # 가위바위보 실시


def rsp(a, b):
    if cards[a] == cards[b]:  # 비긴 경우
        return a
    elif cards[a] - cards[b] == 1 or cards[a] - cards[b] == -2:  # x가 이긴 경우
        return a
    return b


T = int(input())
for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    print(f'#{tc+1} {divide_two(0, N-1)+1}')
#
#
# # 가위바위보 게임
# def RPS(left, right):
#     l, r = cards[left - 1], cards[right - 1]
#
#     # 같을 경우, 인덱스가 낮은 사람이 이긴다.
#     if l == r:
#         return left
#     # 가위
#     elif l == 1:
#         if r == 3:
#             return left
#         elif r == 2:
#             return right
#     # 바위
#     elif l == 2:
#         if r == 1:
#             return left
#         elif r == 3:
#             return right
#     # 보
#     elif l == 3:
#         if r == 1:
#             return right
#         elif r == 2:
#             return left
#
#
# # card game 함수
# def cardGame(low, high):
#     if low == high:
#         return low
#     else:
#         # 중간 인덱스 설정
#         mid = (low + high) // 2
#
#         l = cardGame(low, mid)
#         r = cardGame(mid + 1, high)
#         return RPS(l, r)
#
#
# # 테스트 케이스 T 입력
# T = int(input())
# for tc in range(1, T + 1):
#     # 인원수 N 입력
#     N = int(input())
#
#     # N개의 카드 리스트 입력
#     cards = list(map(int, input().split()))
#
#     # 결과값 ans
#     ans = cardGame(1, N)
#
#     # 결과 출력
#     print('#{} {}'.format(tc, ans))