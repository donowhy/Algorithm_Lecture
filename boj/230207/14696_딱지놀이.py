# N = int(input())
#
# for i in range(0, N):
#     a, *card_a = list(map(int,input().split()))
#     b, *card_b = list(map(int,input().split()))
#     card_a.sort(reverse=True)
#     card_b.sort(reverse=True)
#     print(card_a)
#     print(card_b)
# #카드 하나당 비교해야한다. 같으면 다음 걸로
#
#
#     try:
#         if card_a[i] > card_b[i]:
#             print('A')
#
#         elif card_a[i] < card_b[i]:
#             print('B')
#
#         elif card_a == card_b:
#             print('D')
#
#     except:
#         if len(card_a) < len(card_b):
#             for j in range(len(card_a)):
#                 if card_a[j] > card_b[j]:
#                     print('A')
#
#                 elif card_a[j] < card_b[j]:
#                     print('B')
#
#
#         elif len(card_a) > len(card_b):
#
#             for j in range(len(card_b)):
#                 if card_a[j] > card_b[j]:
#                     print('A')
#
#                 elif card_a[j] < card_b[j]:
#                     print('B')
#
#
#
#     # if card_a[i] > card_b[i]:
#     #     print('A')
#     #     continue
#     #
#     # elif card_a[i] < card_b[i]:
#     #     print('B')
#     #     continue
#     #
#     # elif card_a == card_b:
#     #     print('D')
#     #     continue
#
#
#
#방법 2
N = int(input())

for _ in range(N):
    temp_a = list(map(int, input().split()))[1:]  # 입력을 받되 맨 앞의 개수는 제외하고 저장한다.
    temp_b = list(map(int, input().split()))[1:]  # 입력을 받되 맨 앞의 개수는 제외하고 저장한다.

    for i in range(4, 0, -1):  # 4부터 반대로 돈다.
        if temp_a.count(i) > temp_b.count(i):  # 만약 해당 모양의 개수가 A가 더 많다면
            print("A")
            break
        elif temp_a.count(i) < temp_b.count(i):  # 만약 해당 모양의 개수가 B가 더 많다면
            print("B")
            break
        if i == 1:  # 만약 마지막까지 왔는데 break 되지 않았다면
            print("D")  # D를 출력한다.