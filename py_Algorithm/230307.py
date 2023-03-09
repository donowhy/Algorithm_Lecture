# #곱셈
# import sys
#
# a, b, c = map(int, sys.stdin.readline().split())
#
# def multi(a, n):
#     if n == 1:
#         return a % c
#     else:
#         tmp = multi(a, n // 2)
#         if n % 2 == 0:
#             return (tmp * tmp) % c
#         else:
#             return (tmp * tmp * a) % c
#
#
# print(multi(a, b))
#
#
# '''
# 2147483647
#
#
# 2 4 8 16 32 64 128 256
# 3 9 27 81 243
#
#
# 118 27 129
# '''



# # 1043 거짓말
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# knowList = set(input().split()[1:])
# parties = []
# for _ in range(m):
#     parties.append(set(input().split()[1:]))
#
# for _ in range(m):
#     for party in parties:
#         if party & knowList: #knowList와 party의 비트 연산, 같은 번호가 있다면
#             knowList = knowList.union(party)
#
# cnt = 0
# for party in parties:
#     if party & knowList: #진실을 아는 사람이 파티에 있는 경우, 같이 간 사람들이 파티에 있는 경우
#         continue
#     cnt += 1
#
# print(cnt)
#
#
#
#
#
# import sys
#
# n, m = list(map(int, sys.stdin.readline().split()))
#
# truth = list(map(int, sys.stdin.readline().split()))[1:]
#
# KNOW_TRUTH = 0
# # 유니온 파인드용 부모 리스트. 여기서 0번은 사람으로 사용하지 않고, 진실을 아는 사람으로 친다.
# parent = [i for i in range(n + 1)]
# for person in truth:
#     parent[person] = KNOW_TRUTH
#
#
# # union find 를 하는 이유는 서로 겹치지 않는 그룹 (거짓말을 모르는 그룹과 거짓말을 아는 그룹)으로 나누기 위해서다.
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
#
# def union(a, b):
#     a = find(a)
#     b = find(b)
#
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# parties = []
# for _ in range(m):
#     party = list(map(int, sys.stdin.readline().split()))[1:]
#     # 파티의 참석한 사람들에 대해 2명씩 union 해본다.
#     for i in range(len(party) - 1):
#         union(party[i], party[i + 1])
#     parties.append(party)
#
# answer = 0
#
# for party in parties:
#     know = False
#     for i in range(len(party)):
#         # 진실을 알고 있던 그룹에 속했었을 경우
#         if find(party[i]) == KNOW_TRUTH:
#             know = True
#             break
#     if not know:
#         answer += 1
#
# print(answer)


## 1149 RGB거리

# 1966 프린터 큐큐


# 핵심 아이디어는
#
# imp의 첫번째 값이 최대값이 될 때까지 가장 첫 번째 값을 맨 뒤로 보내는 FIFO를 반복하고, 첫번째 값이 최대값이 되면
# order를 하나 증가시키는 것이다.
# 또한, 원래 문서의 인덱스를 idx에 저장해놓고 imp의 순서가 바뀔 때마다 같이 순서를 바꿔줘야만 한다.
# 그래야 원래 m번째 문서가 언제 출력되는 지를 아니까!
# 상세히 설명하면 다음과 같다.
#
# test_cases를 먼저 받고 이에 따라 for문을 돌려 n, m과 문서의 중요도 imp를 받는다.
# idx변수 생성: 문서 마다 고유 인덱스를 생성하고, m번째 인덱스를 target으로 둔다.
# order 초기화
# while True이므로 무한 반복인데 break가 있기 때문에 if절에 걸리는 조건이 맞으면 반복이 중단된다.
# 만약 imp의 첫 번째 값이 가장 크다면 order를 하나 증가시킨다.
# idx의 첫 번째 값이 target이라면
# order를 출력하고 반복을 중단한다.
# 그렇지 않다면 imp와 idx의 첫 번째 값을 제거한다.
# idx의 첫번째 값이 target이 될 때까지 반복된다.

# test_cases = int(input())
#
# for _ in range(test_cases):
#     n, m = list(map(int, input().split()))
#     imp = list(map(int, input().split()))
#     idx = list(range(len(imp)))
#     idx[m] = 'target'
#
#     # 순서
#     order = 0
#
#     while True:
#         # 첫번째 if: imp의 첫번째 값 = 최댓값?
#         if imp[0] == max(imp):
#             order += 1
#
#             # 두번째 if: idx의 첫 번째 값 = "target"?
#             if idx[0] == 'target':
#                 print(order)
#                 break
#             else:
#                 imp.pop(0)
#                 idx.pop(0)
#
#         else:
#             imp.append(imp.pop(0))
#             idx.append(idx.pop(0))
#
#
# n = int(input())
# p = []
# for i in range(n):
#     p.append(list(map(int, input().split())))
# for i in range(1, len(p)):
#     p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
#     p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
#     p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
# print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))



#9935 문자열 폭발

# import sys
# input = sys.stdin.readline
#
# string = list(input().rstrip())
#
# rep = list(input().rstrip())
# i = 0
# while True:
#     if rep == string[i:i+len(rep)]:
#         string = string[:i] + string[i+len(rep):]
#         i = 0
#
#     if i == len(string):
#         i = 0
#         if string[i:i+len(rep)] != rep:
#             print(''.join(string))
#             break
#         if string[i:i+len(rep)] == rep:
#             print('FRULA')
#             break
#     i += 1
#
#
#
# import sys
#
# # 입력값 처리
# S = sys.stdin.readline().rstrip()
# explosion_string = sys.stdin.readline().rstrip()
#
# # 문자열 폭발 탐색
# while explosion_string in S:
#     S = S.replace(explosion_string, '')
#
# # 결과 출력
# if S:
#     print(S)
# else:
#     print('FRULA')
#
#
#
#
# import sys
#
# # 입력값 처리
# S = sys.stdin.readline().rstrip()
# explosion_string = sys.stdin.readline().rstrip()
#
# # stack으로 문자열 폭발 구현
# stack = []
# ex_len = len(explosion_string)
#
# for i in range(len(S)):
#     stack.append(S[i])
#     if ''.join(stack[-ex_len:]) == explosion_string:
#         for _ in range(ex_len):
#             stack.pop()
#
# # 결과 출력
# if stack:
#     print(''.join(stack))
# else:
#     print('FRULA')
#

#오큰수
# T = int(input())
#
# lst = list(map(int,input().split()))
# arr =[]
# i = 0
# while True:
#     for j in range(i, len(lst)):
#         if lst[i] < lst[j]:
#             arr.append(lst[j])
#             break
#         else:
#             pass
#     else:
#         arr.append(-1)
#
#     i += 1
#
#     if i == len(lst):
#         break
#
# print(*arr)


# import sys
# n = int(input())
# A = list(map(int, sys.stdin.readline().split()))
# answer = [-1] * n #미리 값을 배정해놓음
# stack = []
#
#
# stack.append(0)
# for i in range(1, n):
#     while stack and A[stack[-1]] < A[i]:
#         #스택 값이 있고, 마지막 값이 현재 비교하는 값보다 작다면
#         a = stack.pop()
#         print(a)
#         answer[a] = A[i]
#         print(answer)
#     stack.append(i)
#
#
# print(*answer)


#회의실 배정


# import sys
# n = int(input())
# arr = []
# for i in range(n):
#     a,b = map(int, sys.stdin.readline().split())
#     arr.append([a,b])
#
# stk = [arr[0]]
# for i in range(1, len(arr)):
#     if arr[i][0] >= stk[-1][1]:
#         stk.append(arr[i])
# print(len(stk))

#####

import sys

N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0])) # x가 결과값 : x[1], x[0] 가 값.

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)


#####

n = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
ans = end = 0
for s, e in time:
    if s >= end:
        ans += 1
        end = e
print(ans)


#####
N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])
print(time)
time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순
print(time)
last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)