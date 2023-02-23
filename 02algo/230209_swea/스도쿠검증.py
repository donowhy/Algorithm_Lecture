
#1. 이중 for문을 사용한 방법
# def bf1(p, t, M, N):
#     pass
#     for i in range(N-M+1):
#         for j in range(M):
#             if t[i+j] != p[j]:
#                 break
#         else:
#             return i #패턴이 매칭된 것
#     return -1
#
# p = 'is'
# t = 'This is a book!'
# M = len(p)
# N = len(t)
#
#
# print(bf1(p,t,M,N))

# #2. 슬라이싱을 사용한 방법
# def bf1(p, t, M, N):
#     pass
#     for i in range(N-M+1):
#         # p에서 문자열을 M만큼 가져오고 t와 비교를 수행
#         if  p[i: i +M] == t:
#             return i
#
#     return -1
#
# p = 'is'
# t = 'This is a book!'
# M = len(p)
# N = len(t)
#
#
# print(bf1(p,t,M,N))
# p.find()
#
# #카운트 함수를 만드는데 find함수를 써서
# def count1(p, t, M, N):
#     #카운트하는 변수
#     cnt = 0
#     #인덱스를 저장하는 i 변수
#     i = 0
#     #while문의 조건 작성
#     #find 메소드를 사용해서 i index를 갱신
#     while i != -1:
#         i = p.find(t, i+1)
#         if i != -1:
#             cnt += 1
#     return cnt
#
#     while (i := p.find(t, i+1)) != -1:
#         #조건문 안에 쓸 때 사용가능함
#         cnt += 1
#         return cnt
# #count 메소드
#
# def count2(p,t, M, N):
#     return p.count(t)





import pprint

N = int(input())


for nums in range(N):
    arr = []

    for num in range(9):
        sdoku = list(map(int,input().split()))
        arr.append(sdoku)
    arr_x = list(zip(*arr))

    print(arr_x)
    # print(arr)

    # if len(set(arr[num])) == 9:
    #     if len(set(arr_x[num])) == 9:
    #         print(True)

    for i in range(1, 10, 3):
        for j in range(1, 10, 3):
            print(i, j)

            lst = [arr[i][j], arr[i - 1][j - 1], arr[i - 1][j], arr[i - 1][j + 1], arr[i][j - 1], arr[i][j + 1],
                  arr[i + 1][j - 1], arr[i + 1][j], arr[i + 1][j + 1]]
            print(lst)
            # if len(set(lst)) != 9:
            #         # print(lst)
            #     print(0)

#
# 1
# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9
'''

T = int(input())

sdoku = []
for i in range(9):
    sdoku.append([0,0,0,0,0,0,0,0,0])

for test_case in range(1, T+1):
    answer = 1
    for i in range(9):
        sdoku[i] = input().split()

    for i in range(9):
        for j in range(9):

            for o in range(9):
                if i != o and sdoku[i][j] == sdoku[o][j]:
                    answer -= 1
            for o in range(9):
                if j != o and sdoku[i][j] == sdoku[i][o]:
                    answer -= 1
            for o in range(3):
                for p in range(3):
                    x = ((i // 3) * 3 )+ ((i + o) % 3)
                    y = ((j // 3) * 3 )+ ((j + p) % 3)
                    if i != x and j != y and sdoku[i][j] == sdoku[x][y]:
                        answer -= 1
    if answer < 1:
        answer = 0
    print(f'#{test_case} {answer}')
'''







