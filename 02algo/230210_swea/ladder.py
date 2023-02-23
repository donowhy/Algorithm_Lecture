# ladder
for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)] #2차원 배열로 받기
    # 결과를 저장할 변수
    result_cnt = 100000 # 최대 값
    result = 0 # 결괏값
    # 모든 출발점을 검사
    for n in range(100):
        if arr[0][n] == 1: # 첫 행에서 출발할 수 있는 경우
            cnt = 0  #움진인 거리를 카운트
            x, y = n, 0 # x가 행(좌우), y가 열 (위,아래)
            while 1:
                if x < 99 and arr[y][x+1] == 1: # 오른쪽에 1이 있다면 오른쪽으로 이동
                    while x < 99 and arr[y][x+1] == 1: #오른쪽에 1이 없을 때까지 반복
                        x += 1 #오른쪽으로 이동
                        cnt += 1 #세어주기

                    else:
                        y += 1

                elif x > 0 and arr[y][x-1] == 1: #오른쪽에 1이 없고 왼쪽에만 있다면 왼쪽으로 이동
                    while x > 0 and arr[y][x-1] == 1: #반복
                        x -= 1 #왼쪽으로 이동
                        cnt += 1 #움직였으니까 세어주기
                    else:
                        y += 1 #왼쪽으로 더 이상 이동이 안될경우 밑으로
                # 밑으로 내려가는 횟수는 모두 같으므로 cnt 증가 X
                elif arr[y+1][x] == 1: #아래로
                    y += 1

                if y == 99: # 도착점에 간 경우 움직인 횟수 검사 후 저장
                    if result_cnt >= cnt: #range(100)으로 모두 확인해서
                        result_cnt = cnt #가장 작을 때의 값일 때
                        result = n #최단거리로 갈 수 있는 x값
                    break
    print(f'#{tc+1} {result}')



# 방법 2
T = 10

for t in range(T):
    testcase = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    # 출발 가능한 인덱스를 구함
    startList = []
    for i in range(100):
        if arr[0][i] == 1:
            startList.append(i)


    def cntRoute(startRow):
        col, row = 0, startRow
        cntSide = 0

        while col != 99:
            # 왼쪽에 길이 있을 때
            if 0 <= row - 1 and arr[col][row - 1] == 1:
                while 0 <= row - 1 and arr[col][row - 1] == 1:
                    row -= 1
                    cntSide += 1

            # 오른쪽에 길이 있을 때
            elif 100 > row + 1 and arr[col][row + 1] == 1:
                while 100 > row + 1 and arr[col][row + 1] == 1:
                    row += 1
                    cntSide += 1

            # 왼쪽, 오른쪽에 길이 없을 때 아래로 진행
            col += 1

        return cntSide


    # 추가 이동한 만큼의 양을 담는 리스트 생성
    cntSideList = []
    for i in startList:
        cntSideList.append(cntRoute(i))

    # cntSideList에서 가장 작은 값을 갖는 인덱스의 시작점 출력
    answer = startList[cntSideList.index(min(cntSideList))]
    print(f"#{testcase}", answer)

# Ladder2
# 점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져,
# 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

# 김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

# 사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 최단거리로
# 바닥에 도착하게 되는지 궁금해졌다. 이를 구해보자.

# DFS로 구하는 방법도 있겠지만 그 방법을 사용하지 않고
# 어차피 1층에서 100층까지 이동하는 거리는 어디서 시작하든 똑같으니
# 그 부분은 제외하고 옆으로 이동하는 거리만 계산해서 최솟값을 구했음.
#
# for _ in range(10):
#     test_case = int(input())
#     ladder = [0] * 100
#     for i in range(100):
#         ladder[i] = list(map(int, input().split()))
#
#     start = []  # 시작할 수 있는 부분을 따로 저장함.
#     for idx, i in enumerate(ladder[0]):
#         if i == 1:
#             start.append(idx)
#
#     cnt = [0] * len(start)  # 각 시작점들에 대한 거리를 넣는 변수.
#     for idx, i in enumerate(start):
#         vertex = i  # 호실, 즉 세로줄의 번호를 의미함.
#         floor = 0  # 층수, 즉 가로줄의 번호를 의미함.
#         while floor <= 99:  # 마지막 100층이 되면 반복문 종료.
#
#             # 1호실일 경우 왼쪽 호실은 없으므로 보지 않고 오른쪽 호실만 본다.
#             if vertex == 0:
#
#                 # 오른쪽 호실에 길이 있는지 확인.
#                 # 만약 있다면 cnt에 옆으로 이동한 거리를 저장하고
#                                 # 오른쪽 호실로 이동한 후에 한층 이동.
#                 if ladder[floor][vertex + 1] == 1:
#                     cnt[idx] += start[start.index(vertex) + 1] - vertex
#                     vertex = start[start.index(vertex) + 1]
#                     floor += 1
#                 # 없으면 한층 이동
#                 else:
#                     floor += 1
#
#             # 100호실일 경우 오른쪽 호실은 없으므로 보지 않고 왼쪽 호실만 본다.
#             elif vertex == 99:
#                 # 왼쪽 호실에 길이 있는지 확인.
#                 # 만약 있다면 cnt에 옆으로 이동한 거리를 저장하고
#                                 # 왼쪽 호실로 이동한 후에 한층 이동.
#                 if ladder[floor][vertex - 1] == 1:
#                     cnt[idx] += vertex - start[start.index(vertex) - 1]
#                     vertex = start[start.index(vertex) - 1]
#                     floor += 1
#                 # 없으면 한층 이동
#                 else:
#                     floor += 1
#
#             # 1호실, 100호실이 아닐 경우 오른쪽 호실 확인 후
#                         # 왼쪽 호실에 길이 있는지 확인.
#             # 만약 있다면 cnt에 옆으로 이동한 거리를 저장하고 옆호실로 이동한 후에
#                         # 한층 이동.
#             else:
#                 # 오른쪽에 길이 있는지 확인.
#                 if ladder[floor][vertex + 1] == 1:
#                     cnt[idx] += start[start.index(vertex) + 1] - vertex
#                     vertex = start[start.index(vertex) + 1]
#                     floor += 1
#                 # 없으면 왼쪽에 길이 있는지 확인.
#                 else:
#                     if ladder[floor][vertex - 1] == 1:
#                         cnt[idx] += vertex - start[start.index(vertex) - 1]
#                         vertex = start[start.index(vertex) - 1]
#                         floor += 1
#                     # 없으면 한층 이동
#                     else:
#                         floor += 1
#     print(f'#{test_case} {start[cnt.index(min(cnt))]}')


#방법 4
T = 10
for t in range(T):
    test = int(input())
    #100번돌면서 데이터를 받는다.
    ladder = [list(map(int, input().split())) for _ in range(100)]
    #사다리 길이중 제일 적은길이 저장용
    min_count = 10000
    #제일짧은 사다리의 위치를 저장
    return_x = 0
    #제일뒤부터 앞까지 1인위치를 찾아 저장한다.
    #그냥 range(100)으로 넣어도 상관이없다. 그냥 뒤로했다.
    start_list = [i for i in range(99, -1, -1) if ladder[0][i]]
    #시작할수있는 포인트만큼 반복
    for start in start_list:
        #이동을 위해 좌표셋팅
        #제일 위에서부터 시작하므로 y좌표는 0이다.
        d_y = 0
        #x좌표는 1인곳에서 시작해야하고 그것은 start에 들어있다.
        d_x = start
        #현재 사다리의 이동칸수를 저장하기 위한 변수
        count = 0
        #좌우이동을 방지하기 위한 변수이다.
        move = 0
        #y축이 99가 될때까지 반복한다.
        #99라면 제일 밑이므로 더이상 계산할 필요가 없다.
        down = 0
        left = 1
        right = 2
        while d_y < 99:
            #밑으로 내려갔거나 왼쪽으로 이동했었다면
            #왼쪽으로 갈때 벽이 아닌지 확인하고
            #벽이 아니라면 1인지 체크한다.
            if (move == down or move == left) and d_x > 0 and ladder[d_y][d_x-1]:
                #위의 조건을 통과했다면 왼쪽으로 이동후
                #이동했던 행동을 left로 기록한다.
                d_x -= 1
                move = left
            #밑으로 내려갔거나 오른쪽으로 이동했었다면
            #오른쪽으로 갈때 벽이 아닌지 확인하고
            #벽이 아니라면 1인지 체크한다.
            elif (move == down or move == right) and d_x < 99 and ladder[d_y][d_x+1]:
                #위의 조건을 통과했다면 오른쪽으로 이동후
                #이동했던 행동을 right로 기록한다.
                d_x += 1
                move = right
            #왼쪽도 오른쪽도 못간다면 아래로 내려간다.
            #내려갈수있는지 체크했지만 그냥 else로 적어도 무방하다.
            elif ladder[d_y + 1][d_x]:
                #아래로 이동하고 행동을 down으로 바꾼다.
                d_y += 1
                move = down
            #이동을 할때마다 count를 기록해준다.
            count +=1
            #이동행동을 체크하는 이유는
            #오른쪽으로 이동후 왼쪽과 오른쪽이 1인경우가 생긴다.
            #그때 무한루프에 빠질수있으므로 단방향으로 이동하기위해 사용한다.
        #끝까지 내려왔다면 이동했던 count를 현재 최소카운트와 비교한다.
        if min_count > count:
            #현재 거리가 더짧다면 count를 갱신한다.
            min_count = count
            #출발했던 좌표또한 기록한다.
            return_x = start
    #모두 반복하여 여기까지 왔다면 결과를 출력한다.
    print("#{} {}".format(test, return_x))
