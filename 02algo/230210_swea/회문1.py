import pprint

for tc in range(10):
    pali_num = int(input())
    cnt = 0
    board = []

    for _ in range(8):
        string = input().split()
        board.append(string)

    chk = ''

    for i in range(8):
        for j in range(1):
            for k in range(8 - pali_num + 1):
                letter = board[i][j][k:k + pali_num]
                pali_letter = ''.join(list(reversed(letter)))
                if letter == pali_letter:
                    cnt += 1

    for i in range(8):
        arr = []
        for j in range(8):
            arr.append(board[j][0][i])
        turn = ''.join(arr)

        for l in range(8):
            if len(turn[l:l + pali_num]) == pali_num:
                letter_rev = turn[l:l + pali_num]
                letter_rev_rev = ''.join(list(reversed(letter_rev)))
                if letter_rev == letter_rev_rev:
                    cnt += 1

    print(f'#{tc+1} {cnt}')


# 단어가 어디에 들어갈 수 있을까
#
# def count(arr):
#     ans = 0
#     for lst in arr:
#         cnt = 0
#         for n in lst:
#             if n == 1: #단어를 넣을 수 있는 칸
#                 cnt += 1
#             else:  #칸 없음
#                 if cnt  == k:
#                     ans += 1
#                 cnt = 0
#     return ans
#
# T= int(input())
# for tc in range(1, T + 1):
#     n, k = map(int, input().split())
#     arr = [list(map(int, input().split())) + [0] ]
#
#     arr_t = list(map(list,zip(*arr)))


# 숫자 배열 회전

# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [input().split() for _ in range(n)]
#
#     a1 = [[0] * n for _ in range(n)]
#     a2 = [[0] * n for _ in range(n)]
#     a3 = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             a1[i][j] = arr[n - 1 - j][i]
#             a2[i][j] = arr[n - 1 - i][n - 1 - j]
#             a3[i][j] = arr[j][n - 1 - i]
#
#     print(f'#{tc}')
#
#     for a,b,c in zip(a1,a2,a3):
#         print(f"{''.join(a)} {''.join(b)} {''.join(c)}")

# ladder
# t = 10
# for tc in range(1, t+ 1):
#     _ = int(input())
#     arr = [[0] + list(map(int, input().split())) +[0]]
#
#     mn = 100*100
#
#     for sj in range(1, 101):
#         si = 0
#         if arr[si][sj] != 1:
#             continue
#         cnt, dj = 0, 0
#         ci, cj = si, sj
#         while ci<99:
#             cnt += 1
#             if dj == 0:
#                 if arr[ci][cj-1] == 1: # 좌측
#                     dj = -1
#                     cj -= 1
#                 elif arr[ci][cj+1]== 1  #우측
#                     dj = 1
#                     cj += 1
#                 else:
#                     ci += 1
#             else:
#                 if arr[ci][cj+dj] == 1:
#                     cj += dj
#                 else:  # 진행방향이 막힌경우 아래로
#                     dj = 0
#                     ci += 1
#
#         if mn >= cnt:
#             mn, ans = cnt, sj -1
#
# print(f'#{tc} {ans}')
#
