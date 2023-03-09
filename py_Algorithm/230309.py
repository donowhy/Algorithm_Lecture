# #15988 1,2,3 더하기 3
#
#
# t = int(input())
#
# dp = [0] * 1000001
#
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# for k in range(t):
#     n =int(input())
#     for i in range(4,n+1):
#         dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
#     print(dp[n])



#13305 주유소

# cities = int(input())
# distance = list(map(int,input().split()))
# price = list(map(int,input().split()))
#
# dist = []
# ga = []
# i = 0
# hap = 0
# while i < cities -1:
#     if price[i] <= price[i+1]:
#         dist.append(distance[i])
#         ga.append(price[i])
#
#     elif price[i] > price[i+1]:
#         if dist and ga:
#             dist.append(distance[i])
#             hap += sum(dist) * ga[0]
#             dist = []
#             ga = []
#         else:
#             hap += distance[i] * price[i]
#
#     i += 1
#
# if dist and ga:
#     hap += sum(dist) * ga[0]
# print(hap)
#
#
#
#
#
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
#
# roads = list(map(int, input().split()))
# costs = list(map(int, input().split()))
#
# # 첫번째 값 더하기
# min_price = roads[0] * costs[0]
#
# # 가장 값이 싼 주유소 지정
# min_cost = costs[0]
#
# for i in range(1, N - 1):
#     if min_cost > costs[i]:  # 가장 값이 싼 주유소가 현재 주유소 보다 비싸면 바꿔준다.
#         min_cost = costs[i]  # 값 싼 주유소로 바꿔주기
#
#     min_price += min_cost * roads[i]
#
# print(min_price)
# '''
# 5
# 200000000 300000000 500000000 400000000
# 500000000 600000000 800000000 700000000 500000000
#
# 4
# 5 5 5
# 1000000000 999999999 999999998 10
#
# 7
# 3 4 2 2 4 5
# 8 9 5 4 2 7 1
#
# '''

#2800

import sys
from itertools import combinations

n = list(map(str, sys.stdin.readline().strip()))
answer = set()
stack = []
temp = []

# 반복문을 통해 괄호의 시작점과 끝점을 저장
for idx, word in enumerate(n):
    if word == "(":
        stack.append(idx)
    elif word == ")":
        temp.append((stack.pop(), idx))

for i in range(1, len(temp) + 1):
    c = combinations(temp, i) # combinations을 통해 모든 경우의 수를 확인

    # 반복문을 통해 경우의 수를 확인
    for j in c:
        target = list(n)

        # 괄호 제거
        for k in j:
            target[k[0]] = ""
            target[k[1]] = ""

        answer.add(''.join(target))

for ans in sorted(list(answer)):
    print(ans)




from itertools import combinations
import sys

input = sys.stdin.readline

s = input().rstrip()

l = []
stack = []
answer = set()

for idx, v in enumerate(list(s)):
    if v == '(':
        stack.append(idx)
    elif v == ')':
        start = stack.pop()
        end = idx
        l.append([start,end])

for i in range(1,len(l)+1):
    combi = combinations(l,i)
    for j in combi:
        tmp = list(s)
        for k in j:
            start,end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))


for i in sorted(list(answer)):
    print(i)