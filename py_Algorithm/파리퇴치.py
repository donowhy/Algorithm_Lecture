# garo, sero = map(int, input().split())
# lst = []
# ans = []
# #1 북쪽 2 남쪽 3 서쪽 4 동쪽
# for i in range(int(input())):
#     x, y = map(int,input().split())
#     lst.append([x, y])
#
# a, b = map(int, input().split())
#
# print(lst)
# for i in range(int(input())):
#     if lst[i][0] == 1:
#         if a == 1:
#             ans.append(abs(lst[i][1] - b))
#         if a == 2:
#             if a // 2 <= lst[i][1] and a // 2 <= y:
#                 ans.append(sero + a - lst[i][1] + y )
#
#             elif a // 2 <= lst[i][1] and a // 2 >= y:
#                 ans.append(sero + lst[i][1] + y)
#
#             elif a // 2 >= lst[i][1] and a // 2 <= y:
#                 ans.append(sero + lst[i][1] + y)
#
#             elif a // 2 >= lst[i][1] and a // 2 >= y:
#                 ans.append(sero + lst[i][1] + y)
#
#
#
#
#
#
#
#
#
#
# import sys
# input=sys.stdin.readline
#
# #북쪽 왼쪽 모서리를 0으로 잡고 펼쳤을 때 0으로부터 얼마나 떨어졌는 지 위치를 계산해주는 함수
# def cal_dist(loc, distance) :
#     if loc==1 : #북쪽
#         return distance
#     elif loc==4 : #동쪽
#         return w+distance
#     elif loc==2 : #남쪽
#         return w+h+w-distance
#     elif loc==3 : #서쪽
#         return w+h+w+h-distance
#
#
# #블록의 가로길이 세로길이 입력받기
# w, h = map(int,input().split())
#
# #상점의 개수 입력받기
# num=int(input())
#
# #상점의 위치를 저장할 리스트 만들어 놓기
# locations=[0]*(num+1)
#
# dist=[]
# #각 상점의 위치와 동근이의 위치 입력받기
# for i in range(num+1) :
#     loc, distance=map(int, input().split())
#     dist.append(cal_dist(loc, distance))
#
# #동근이의 0에서 부터 떨어진 위치를 저장
# dong_dist=dist[-1]
#
#
# answer=0
# for i in range(num):
#     #0에서 떨어진 각 가게의 거리와, 0에서 떨어진 동근의 위치 차이의 절댓값을 구해준다.
#     cal_distance=abs(dist[i]-dong_dist)
#
#     #전체 길이를 구해준다.
#     total=2*(w+h)
#
#     #더 작은 값을 answer에 누적시킨다.
#     answer+=min(cal_distance,total-cal_distance)
#
# print(answer)

from collections import deque

N, L = map(int,input().split())
lst = []
for xxx in range(N):
    loc, R, G = map(int,input().split())
    lst.append([loc,R,G])

t = 0
i = 0

while L > 0:
    t += 1
    L -= 1
    if t == lst[i][0]:
        if t < (lst[i][1] + lst[i][2]):
            if t % (lst[i][1] + lst[i][2]) > lst[i][1]:
                pass
            else:
                t += lst[i][1] - lst[i][0] % (lst[i][1] + lst[i][2])

        else:
            if t % (lst[i][1] + lst[i][2]) < lst[i][1]:
                t += lst[i][1] - lst[i][0] % (lst[i][1] + lst[i][2])
            else:
                pass

        lst.pop()
print(t)


import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pos = 0
answer = 0

for _ in range(N):
    d, r, g = map(int, input().split())

    answer += (d - pos)
    pos = d
    if answer % (r+g) <= r:
        answer += (r - (answer%(r+g)))

answer += (L-pos)
print(answer)
'''
2 10
3 3 3
5 2 3
'''
