from collections import deque

def bfs():


R,C,T = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(R)]
dq = deque()
arr = [[0]* C for _ in range(R)]

for i in range(R):
    for j in range(C):
