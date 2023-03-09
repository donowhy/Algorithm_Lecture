import pprint

N = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(1, N+1):
    M = int(input())
    arr = [[0]*M for _ in range(M)]

    direction = x = y = 0

    for j in range(1,M*M+1):

        arr[x][y] = j

        x += dx[direction]
        y += dy[direction]


        if x<0 or y<0 or x>=M or y>=M or arr[x][y]:
            x -= dx[direction]
            y -= dy[direction]

            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]


    print(f'#{i}')
    for k in range(len(arr)):
        print(*arr[k])



#방법 2
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for i in range(N)]

# 재귀함수 작성
    def snail_number(start, N):

# cnt를 하나씩 증가시키며 작성
# 위에서부터 4개, 오른쪽 3개, 아래쪽 3개, 왼쪽 2개를 작성하여 테두리 먼저 작성.
# 시작점을 (1,1)로 옮기고 N을 2만큼 감소시킨 후 다시 함수 실행(재귀함수)
# 그 다음 안쪽 테두리 완성....(반복)
        global cnt
# 윗부분 완성
        for i in range(N):
            snail[start][i + start] = cnt
            cnt += 1
# 오른쪽 부분 완성
        for i in range(1, N):
            snail[i + start][N - 1 + start] = cnt
            cnt += 1
# 아랫부분 완성
        for i in range(1, N):
            snail[N - 1 + start][N - 1 - i + start] = cnt
            cnt += 1
# 왼쪽 부분 완성
        for i in range(1, N - 1):
            snail[N - 1 - i + start][start] = cnt
            cnt += 1
# 종료 조건
        if N < 2:
            return snail
        return snail_number(start + 1, N - 2)


    cnt = 1
    start = 0
    print(f'#{test_case}')
    for i in snail_number(start, N):
        print(*i)
