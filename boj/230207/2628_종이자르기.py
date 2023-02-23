#첫 줄 가로 세로 길이 최대는 100
#칼로 잘라야 하는 점선의 갯수
# 가로는 0 과 점선번호
# 세로는 1과 점선번호
#첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다
'''
10 8
3
0 3
1 4
0 2
'''
#
# r, c = map(int, input().split())
# #자르는 위치 저장
# row = [0, r]    # [0, 10]
# column = [0, c] #  [0, 8]
#
# for _ in range(int(input())):   # 자르는 횟수
#     rr, linenumber = map(int, input().split())
#     if rr == 1:             # 세로가 1 가로가 0-> 세로는 r에 가로는 c
#         row.append(linenumber)
#     else :
#         column.append(linenumber)
#
# row.sort()     # [0, 4, 10]
# column.sort()  # [0, 2, 3, 8]
#                # 빼서 최대 길이 구하기
#
# subtracted_r = []  #[4, 6]
# subtracted_c = []  #[2, 1, 5]
#
# for i in range(len(row)-1):    # 0 1
#     subtracted_r.append(row[i + 1] - row[i])   # row[1]-row[0]   row[2]-row[1]
# for i in range(len(column) -1): # 0 1 2
#     subtracted_c.append(column[i+1]- column[i]) #col[1]-col[0]  col[2]-col[1]  col[3]-col[2]
#
# print(max(subtracted_r) * max(subtracted_c))

#
# #방법 2
x, y = map(int, input().split())
x_list = [0, x]  # 가로 각각 길이
y_list = [0, y]  # 세로 각각 길이
for _ in range(int(input())):
    xy, length = map(int, input().split())
    if xy == 0:
        y_list.append(length)
    else:
        x_list.append(length)

x_list.sort()  # 좌, 위쪽부터 꺼내서 대조 하기 위함
y_list.sort()

max_square = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i - 1]
        height = y_list[j] - y_list[j - 1]
        max_square = max(max_square,width * height)  # 가장 큰 범위
        print(max_square)
print(max_square)
#
# #방법3
#
# c, r = map(int, input().split())
# N = int(input())
# rarr = [0]
# carr = [0]
#
# for i in range(N):
#     t, p = map(int, input().split())
#     if t == 0:
#         rarr.append(p)
#     else:
#         carr.append(p)
# rarr.append(r)
# carr.append(c)
# rarr.sort()
# carr.sort()
# maxr = 0
# for i in range(1, len(rarr)):
#     gap = rarr[i] - rarr[i-1]
#     if maxr < gap:
#         maxr = gap
# maxc = 0
# for i in range(1, len(carr)):
#     gap = carr[i] - carr[i-1]
#     if maxc < gap:
#         maxc = gap
#
# print(maxr * maxc)


