from collections import deque

def room():
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    for i in range(N):
        for j in range(N):
            dq.append([i,j])

    while dq:
        cnt = 1
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N -1 or ny > N - 1 or visited[nx][ny]:
                continue
            else:
                if arr[nx][ny] == arr[x][y] + 1:
                    visited[nx][ny] = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                lst.append([i,j])


    for i in range(len(lst)-1):
        if lst[i][0] == lst[i+1][0]:
            res.append(lst[i+1][1] - lst[i][1] + 1)
        elif lst[i][1] == lst[i+1][1]:
            res.append(N - 1 + 1)


    print(res)
    print(lst)

    print(visited)


for t in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dq = deque([])
    lst = []
    res = []
    board = []
    cnt = 0
    room()

    print(f'#{t+1} {cnt} {max(res)}')




####
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def search(start):
    global N

    cnt = 0
    stack = [start]
    while stack:
        x, y = stack.pop()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y] + 1 == arr[nx][ny]:
                    stack.append((nx, ny))
    return cnt



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    answer = [float('inf'), 0]

    for i in range(N):
        for j in range(N):
            cnt = search((i, j))
            if cnt > answer[1]:
                answer[1] = cnt
                answer[0] = arr[i][j]
            elif cnt == answer[1]:
                if arr[i][j] < answer[0]:
                    answer[0] = arr[i][j]

    print(f'#{tc} {answer[0]} {answer[1]}')



####
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for t in range(T):
    N = int(input())
    mapp = []
    max_cnt = 0  # 결과값 / 이동한 방의 최대 개수가 저장될 변수
    room = 999999999999  # 결과값 2 / 시작 방번호가 저장될 변수
    for _ in range(N):
        mapp.append(list(map(int, input().split())))
    for x in range(N):  # 모든 x,y 탐색
        for y in range(N):
            cnt = 1
            q = [(x, y)]  # 첫 시작 방 위치 queue에 저장
            while q:  # BFS 탐색 시작 / q가 빌 때까지 q의 요소를 pop 해서 4방향 탐색 조건 만족시 append
                qq = q.pop()
                for i in range(4):
                    if 0 <= qq[0] + dx[i] < N and 0 <= qq[1] + dy[i] < N and (
                            mapp[qq[0] + dx[i]][qq[1] + dy[i]] - mapp[qq[0]][qq[1]] == 1):
                        cnt += 1
                        q.append((qq[0] + dx[i], qq[1] + dy[i]))
            if cnt > max_cnt:  # 탐색 종료 후 건너온 방의 개수가 현재까지 저장된 최대 방 건너온 개수와 비교해서 더 많다면
                max_cnt = cnt  # cnt가 이제 최대 방 건너온 개수가 됨
                room = mapp[x][y]  # room에 위치 저장
            elif cnt == max_cnt:  # 건너온 개수가 같다면
                if mapp[x][y] < room:  # 저장된 방 번호와 비교해 작은지 판단
                    room = mapp[x][y]

    print('#{} {} {}'.format(t + 1, room, max_cnt))



####
def iswall(x, y):  # 벽 체크 맵의 범위안에 있는지 + 다음칸과의 차가 1인지
    if (0 <= x < n) and (0 <= y < n) and (arr[x][y] - arr[x - dx[i]][y - dy[i]] == 1):
        return False
    return True


T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_cnt = 0  # 결과값 / 이동한 방의 최대 개수가 저장될 변수
    room = 9999999  # 결과값 2 / 시작 방번호가 저장될 변수
    for x in range(n):  # 모든 x,y 탐색
        for y in range(n):
            init_x = x  # x와 y가 탐색을 하며 변동 되므로 최초 위치를 따로 저장함. 나중에 cnt와 room 비교를 위해 필요함
            init_y = y
            cnt = 1
            idx = 0  # for문 돈 횟수
            i = 0
            while 1:
                if idx > 4:  # 현재 위치에서 4방향을 다 돌고도 갈 곳이 없다면 종료
                    break
                if iswall(x + dx[i], y + dy[i]) == False:
                    x += dx[i]
                    y += dy[i]
                    cnt += 1
                    idx = 0  # 벽체크 후 갈 수 있다면 한칸 간 후 다시 4방향 체크를 할 것이기에 0으로 초기화
                    i = 0
                else:
                    i += 1
                    idx += 1
                if i == 4:
                    i = 0
            if cnt > max_cnt:
                max_cnt = cnt
                room = arr[init_x][init_y]
            elif cnt == max_cnt:
                if room > arr[init_x][init_y]:
                    room = arr[init_x][init_y]
    print('#{} {} {}'.format(t + 1, room, max_cnt))