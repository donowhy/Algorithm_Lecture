T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ai = input()
    lst = []
    dict = {}
    for i in ai:
        lst.append(i)

    for card in lst:
        cnt = 0
        for num in range(len(lst)):
            if card == ai[num]:
                cnt += 1
        dict[card] = cnt
        aa = list(dict)
        aa.sort()
        # print(dict)
    for key, value in dict.items():
        if value == max(dict.values()):
            if max(dict.values()) == 1:
                print(f'#{test_case} {aa[-1]} 1')
                break
            else:
                print(f'#{test_case} {key} {max(dict.values())}')



# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     cards = input()
#     cnt = [0] * 10
#
#     for i in range(N):
#         cnt[int(cards[i])] += 1
#
#     max_id = 0
#     for i in range(10):
#         if cnt[max_id] <= cnt[i]:
#             max_id = i
#
#     print(f'#{tc} {max_id} {cnt[max_id]}')