import sys
sys.stdin = open('input.txt', 'r')
import pprint
from itertools import combinations


input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(M)]

chk = []
for i in range(N):
    for j in range(M):
        chk.append((i,j))


pprint.pprint(arr)
pprint.pprint(chk)

for i in range(N):
    for j in range(M):
        if chk[i+1][0] - chk[i][0] == 1 :



#방법 1
import sys

input = sys.stdin.readline

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# INPUT
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최대값 변수
maxValue = 0


# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt + 1)
            visited[ni][nj] = False


# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j):
    global maxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n + k) % 4
            ni = i + move[t][0]
            nj = j + move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxValue)


#방법 2

import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)

#방법 3

import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if idx == 3:
        if total > ans:
            ans = total
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    dfs(nr, nc, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0

def block(r, c, total):
    global ans
    make_block = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            make_block += 1
            total += arr[nr][nc]

    if make_block == 3:
        if total > ans:
            ans = total

    if make_block == 4:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            total -= arr[nr][nc]
            if total > ans:
                ans = total
            total += arr[nr][nc]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        block(r, c, arr[r][c])
        visit[r][c] = 0

print(ans)

#방법 4
import sys; input = sys.stdin.readline

def dfs(x, y, step, total):
    global answer
    # 종료조건1) 탐색을 계속 진행하여도 최댓값에 못 미치는 경우
    if total + max_val*(4-step) <= answer:
        return

    # 종료조건2) 블록 4개를 모두 활용한 경우
    if step == 4:
        answer = max(answer, total)
        return

    # 상하좌우 방향으로 블록 이어 붙여 나가기
    for dx, dy in d:
        nx = x + dx # 새로운 x 좌표
        ny = y + dy # 새로운 y 좌표
        # 새로운 좌표가 유효한 범위 내 있고 탐색이력이 없는 경우
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            # 2번째 블록 연결 후 'ㅏ','ㅓ','ㅗ','ㅜ' 만들기
            if step == 2:
                visited[nx][ny] = True # 탐색기록
                # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색재개
                dfs(x, y, step+1, total+board[nx][ny])
                visited[nx][ny] = False # 탐색기록 제거

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = False

if __name__ == "__main__":
    N, M = map(int, input().split()) # 좌표의 행, 열 개수
    board = [list(map(int, input().split())) for _ in range(N)] # 좌표별 값
    max_val = max(map(max, board)) # 모든 좌표 중 최댓값
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌표 내 상하좌우
    visited = [[False] * M for _ in range(N)] # 탐색여부 확인용
    answer = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = True # 탐색기록
            dfs(i, j, 1, board[i][j])
            visited[i][j] = False # 탐색기록 제거
    print(answer)
