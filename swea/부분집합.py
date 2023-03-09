# # 정수 10개의 입력을 받는다.
# arr = list(map(int, input().split()))
#
# def is_zero_subset(arr):
#     """
#     #부분집합의 합이 0이 되도록 하는 값이 존재하는지 확인하는 함수
#     :param arr: 정수 10개의 배열
#     :return: 합이 0이 되는 부분집합이 있다면 True를 반환 없다면 False를 반환
#     """
#
#     # 부분집합
#     n = len(arr)
#     #부분 집합을 만들 수 있는 개수
#     for i in range(1, 1<<n):
#         hap = 0 #합을 확인할 수 있는 변수
#         for j in range(n):
#             if i & (1<<j):
#                 #이 안에서 합을 진행하는 코드
#                 print(arr[j], end = '')
#                 hap += arr[j]
#         # 0 이 된다면 True를 반환
#         if hap == 0:
#             return True
#     return False
#
#
# arr = list(map(int,input().split()))
# print(is_zero_subset())

'''
3
3 6
5 15
5 10
'''

from itertools import combinations
import pprint

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

N = int(input())
for i in range(N):
    a, b = map(int,input().split())
    lst = list(combinations(arr, a))
    hap = 0
    # pprint.pprint(lst)
    count = 0
    for j in lst:
        if sum(j) == b:
            count += 1
    print(f'#{i+1} {count}')
    # for j in range(len(lst)):
        # for k in range(a):
        #     hap += lst[j][k]
        #     if hap == b:
        #         print(lst[j])
        #     elif hap != b:
        #         print('0')


