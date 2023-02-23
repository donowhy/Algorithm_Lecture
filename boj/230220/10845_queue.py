# import sys
#
# N = int(sys.stdin.readline())
#
# queue = []
#
# for i in range(N):
#     cmd = sys.stdin.readline().split()
#
#     if cmd[0] == "push":
#         queue.insert(0, cmd[1]) # 0 이 맨뒤가 됨
#
#     elif cmd[0] == "pop":
#         if len(queue) != 0:
#             print(queue.pop())
#         else:
#             print(-1)
#
#     elif cmd[0] == "size":
#         print(len(queue))
#
#     elif cmd[0] == "empty":
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#
#     elif cmd[0] == "front":
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])
#
#     elif cmd[0] == "back":
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#
#
# # 큐 2
# import sys
# from collections import deque
#
# queue = deque()
# N = int(sys.stdin.readline())
#
# for _ in range(N):
#     i = sys.stdin.readline().split()
#
#     if i[0] == 'push':
#         queue.append(int(i[1]))
#
#     elif i[0] == 'pop':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[0])
#             queue.popleft()
#
#     elif i[0] == 'size':
#         print(len(queue))
#
#     elif i[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#
#     elif i[0] == 'front':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[0])
#
#     elif i[0] == 'back':
#         if not queue:
#             print(-1)
#         else:
#             print(queue[-1])
#
# #방법 1
# input = int(input())
# square = 2
#
# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break
#
#
# #방법 2
# from collections import deque
#
# N = int(input())
# deque = deque([i for i in range(1, N + 1)])
#
# while (len(deque) > 1):
#     deque.popleft()
#     deque.append(deque.popleft())
#
# print(deque[0])
#
#
#
# #방법 3
# import sys
#
# N = int(sys.stdin.readline())
#
# arr = [i + 1 for i in range(N)]
#
# while len(arr) > 1:
#     if len(arr) % 2:
#         t = [arr[-1]]
#         t.extend(arr[1::2])
#         arr = t
#     else:
#         arr = arr[1::2]

# print(arr[0])



