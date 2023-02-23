# from collections import deque
#
# N, K = map(int, input().split())
# belt = deque(list(map(int, input().split())))
#
# cnt = 0
#
# while True:
#     cnt += 1
#     print(belt)
#     belt[0] = belt[0] - 1
#     if belt[0] == 0:
#         # print(belt)
#         K -= 1
#         if K == 0:
#             cnt += 1
#             break
#
#     belt.appendleft(belt.pop())
#
# print(cnt)


# 함수로 풀기
#
# from copy import deepcopy
#
# N, K = map(int, input().split())
#
# robots = []
# belts = list(map(int, input().split()))  # 컨베이어 벨트 - 1차원 리스트로 표현(2*N개)
# belts.insert(0, -1)  # dummy
# is_robot = [False for _ in range(len(belts))]  # 컨베이어 벨트의 index 위치에 로봇이 있는지 확인하기 위함
#
#
# def rotate():
#     # 컨베이어 벨트 및 벨트 위 로봇 회전
#     global belts, is_robot, robots
#     # 벨트 회전
#     n = belts.pop()
#     belts.insert(1, n)
#
#     # 로봇 회전
#     new_robot = []  # 회전 후 로봇 저장
#     is_robot = [False for _ in range(len(belts))]  # 로봇 존재 여부 초기화
#     for belt_index in robots:
#         next_belt_index = belt_index + 1  # 다음 칸으로 이동
#         if next_belt_index < N:  # 다음 칸이 N이하인 경우 새 로봇 배열에 추가 -> 다음 칸이 N인 경우 제외(내린것으로 판단)
#             new_robot.append(next_belt_index)
#             is_robot[next_belt_index] = True
#     robots = deepcopy(new_robot)  # 기존 로봇 배열과 교환
#
#
# def move_robots():
#     # 로봇 이동
#     global is_robot, robots, belts
#     new_robots = []  # 새로운 로봇 배열
#     for belt_index in robots:
#         next_index = belt_index + 1  # 다음 로봇 위치
#         if is_robot[next_index] or belts[next_index] < 1:  # 이동이 불가능한 경우(로봇이 있거나 내구도 1미만)
#             new_robots.append(belt_index)
#         else:  # 이동이 가능한 경우
#             belts[next_index] -= 1  # 다음 위치의 벨트 내구도 1 감소
#             is_robot[belt_index] = False  # 현재 위치에 로봇이 존재하지 않게됨
#             if next_index != N:  # 다음 위치가 N이 아닌경우에만(중요)
#                 new_robots.append(next_index)  # 새로운 로봇 배열에 추가
#                 is_robot[next_index] = True
#     robots = deepcopy(new_robots)
#
#
# def insert_robot():
#     global is_robot, robots
#     if belts[1] != 0:  # 1번째 벨트의 내구도가 0이 아닌경우
#         robots.append(1)  # 새로운 로봇 위치(1번째) 추가
#         # 내구도 감소 및 로봇 존재 여부 기록
#         belts[1] -= 1
#         is_robot[1] = True
#
#
# def is_finish():
#     # 0의 개수가 K개 이상이 경우 True 아닌 경우 False 반환
#     return belts.count(0) >= K
#
#
# cnt = 0
# while not is_finish():  # is_finish() 함수가 True를 반환할 때 까지 반복
#     cnt += 1
#     # 1. 컨베이어 및 로봇 회전
#     rotate()
#     # 2. 로봇 이동
#     move_robots()
#     # 3. 로봇 삽입
#     insert_robot()
#
# print(cnt)


#방법 2

from collections import deque

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0] * 2 * n)

level = 0
while 1:
    level += 1  # 단계 1씩 증가
    belt.rotate(1)
    # print(belt,'벨트')
    robots.rotate(1)
    # print(robots, '로봇')
    robots[n - 1] = 0  #robots idx 2 일 때 즉 n값일 떄 0으로 초기화
    for i in range(n - 2, -1, -1): # 2, 1, 0 으로
        if robots[i] and not robots[i + 1] and belt[i + 1]:  #robot의 현재 위치와 바로 앞에 로봇이 없을 경우, 그리고 내구도가 0이 아닌경우
            belt[i + 1] -= 1  #벨트의 내구도는 1 감소
            robots[i + 1], robots[i] = robots[i], 0  #로봇의 위치를 앞으로 한칸
    robots[n - 1] = 0 # robot 의 idx 값이 n 일 때 0으로 갱신
    if not robots[0] and belt[0]:  #올리는 벨트 위에 로봇이 없을 때
        robots[0] = 1  # 로봇 올리기
        belt[0] -= 1  # 내구도 감소
    if belt.count(0) >= k:  # 벨트의 내구도 0인 값이 k보다 값이 같거나 클 때
        print(level)
        break








# #방법 3
#
# import sys
#
# input = sys.stdin.readline
# from collections import deque
#
# n, k = map(int, input().split())
# belt = deque(list(map(int, input().split())))
# robot = deque([0] * n)
# res = 0
#
# while 1:
#     belt.rotate(1)
#     robot.rotate(1)
#     robot[-1] = 0  # 로봇이 내려가는 부분이니 0
#     if sum(robot):  # 로봇이 존재하면
#         for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
#             if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
#                 robot[i + 1] = 1
#                 robot[i] = 0
#                 belt[i + 1] -= 1
#         robot[-1] = 0  # 이 부분도 로봇 out -> 0임
#     if robot[0] == 0 and belt[0] >= 1:
#         robot[0] = 1
#         belt[0] -= 1
#     res += 1
#     if belt.count(0) >= k:
#         break
#
# print(res)