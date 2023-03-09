
# n, k = map(int,input().split())
# val = []
# for _ in range(n):
#     val.append(int(input()))
# dp = [0] * 10001
# dp[0] = 1
# for i in val:
#     for j in range(i, k +1):
#         dp[j] += dp[j-i]
#
# print(dp)

from collections import deque

T = int(input())
lst = deque(list(map(int,input().split())))

stk = []
while lst:
    a = lst.popleft()
    if stk:
        if stk[-1] < a:
            stk.append(a)
        elif stk[-1] > a:
