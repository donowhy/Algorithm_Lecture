# # 입력된 tree에 종속되는 sub_tree의 함수 작성
# def make_tree(n):
#     global count
#
#     # N값이 넘어가지 않아야함
#     if n <= N:
#         # 왼쪽노드는 현재 인덱스의 2배
#         # 예) 6인 경우 1 - 2 - 4 / 3 - 6
#         make_tree(n * 2)  # 함수 안에 함수(재귀함수) 활용
#
#         # 최하단 노드까지 갔으면 값 넣기
#         tree[n] = count
#         count += 1  # 다음값을 넣기 위해 count 증가
#
#         # 오른쪽노드는 인덱스 2배 +1
#         make_tree(n * 2 + 1)
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#
#     # 트리표시를 위한 리스트
#     tree = [0 for i in range(N + 1)]
#     count = 1
#     make_tree(1)  # 함수에 가장 하단 왼쪽노드값인 1 대입
#
#     print(f'#{tc} {tree[1]} {tree[N // 2]}')
#
#     import sys
#
#     sys.stdin = open("input.txt")
#
#     T = int(input())
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
#
#
#
#
#
# def in_order(v):    # 완전 이진 트리 탐색(중위 순회)
#     global cnt, result
#     if v <= n:      # n까지 확인
#         in_order(v * 2)
#         cnt += 1    # 확인할 때마다 cnt + 1
#         if v == 1:  # 조상 노드 값 담기
#             result[0] = cnt
#         elif v == n // 2:   # 조상 노드 // 2 값 담기
#             result[1] = cnt
#         in_order(v * 2 + 1)
#
#
# t = int(input())
# for tc in range(1, t + 1):
#     n = int(input())
#     cnt = 0     # 노드에 저장된 값
#     result = [0, 0]     # 루트 노드에 저장된 값, n // 2 노드에 저장된 값
#     in_order(1)
#     print(f'#{tc}', *result)
#
#
#
# def inorder(node):
#     global cnt
#
#     if node <= n:
#         inorder(node * 2)  # 왼쪽 노드
#         tree[node] = cnt  # 왼쪽 다 다녀 왔으면 값 넣어
#         cnt += 1
#         inorder(node * 2 + 1)  # 오른쪽 노드
#
#
# tc = int(input())
#
# for idx in range(1, tc + 1):
#     n = int(input())  # 이진 탐색 트리에 저장할 노드 개수
#
#     tree = [0 for _ in range(n + 1)]
#
#     cnt = 1
#     inorder(1)  # 중위순회 하면 오름차순으로 정렬된 값을 얻을 수 있다.
#
#     print('#{} {} {}'.format(idx, tree[1], tree[n // 2]))

from heapq import *

# def enqueue(item):
#     # 완전 이진 트리... 맨 마지막에 값을 추가...
#     global hsize
#     c = hsize
#     c += 1
#     hq[c] = item
#
#     p = c // 2
#
#     # 힙(heapify)의 형태... 자리바꾸기...
#     while p and hq[p] > hq[c]:
#         hq[p], hq[c] = hq[c], hq[p]
#         c = p
#         p = c // 2

from heapq import *


for t in range(1, int(input()) + 1):
    n = int(input())
    hq =list(map(int,input().split(',')))
    heapify(hq)
    hq.insert(0,0)
    print(hq, 'hqhqhqhq')
    lst = []
    for i in hq:
        heappush(lst, i)

    print(lst)
    hap = 0
    while n > 1:
        n = n // 2
        hap += lst[n]
    print(f'#{t} {hap}')

#
# import random
# lst = []
# for i in range(1001):
#
#     lst.append(random.randint(1, 1001))
# print(lst)