
for tc in range(1,11):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]

    result = 0  # 총합을 넣을 수 있는 변수

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(n): # x좌표
        hap = 0
        for j in range(n): #(x, y) : (i + dx, j + dy)
            # board[i][j]
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < n:
                    board[x][y]
                    hap += abs(board[i][j] - board[x][y])
        result += hap
    print(f'#{tc} {result}')