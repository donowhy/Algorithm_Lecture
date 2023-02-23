# #회전
# tc = int(input())
#
# for i in range(tc):
#     a, b = map(int,input().split())
#
#     lst = input().split()
#     for _ in range(b):
#         lst.append(lst.pop(0))
#
#     print(f'#{i+1} {lst[0]}')


# # 거듭제곱
# tc = int(input())
#
# for i in range(tc):
#     num = int(input())
#     stk = []
#     for j in range(10 ** 6+1):
#         if j ** 3 == num:
#            stk.append(j)
#         else:
#             stk.append(-1)
#     if max(stk) > -1:
#         print(f'#{i+1} {max(stk)}')
#     else:
#         print(f'#{i+1} -1')



# # 피자 굽기
# tc = int(input())
#
# for i in range(tc):
#     a, b = map(int,input().split())
#     lst = list(map(int,input().split()))
#
#     queue = []
#
#     for j in range(a):
#         queue.append((j, lst.pop(0)))
#
#     while len(queue) >= 1:
#         if queue[0][1]//2 != 0:
#             queue.append(queue.pop(0)[1] // 2)
#
#         else:
#             queue.pop(0)
#             if len(lst) >= 1:
#                 queue.append(lst.pop(0))
#
#         if len(queue) == 2:
#             if queue[0][1] // 2 == 0:
#                 queue.pop(0)
#                 print(queue)

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    pizza_lst = list(map(int, input().split()))
    fire = []

    i = 1
    while True:
        if len(fire) < n and len(pizza_lst) != 0:
            fire.insert(0, [pizza_lst.pop(0), i])
            i += 1
        else:
            fire[0][0] //= 2
            print(fire[0][0])
            if fire[0][0] == 0:
                fire.pop(0)
                if len(fire) == 1:
                    break
                continue
        fire.append(fire.pop(0))
        print(fire, '삭제, 추가')
    print(f'#{tc} {fire[0][1]}')