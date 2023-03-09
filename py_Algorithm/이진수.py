# T = int(input())
# for tc in range(1,T+1):
#     N = float(input())
#     result = []
#     cnt = 0
#     state = False
#     while cnt < 12:
#         N *= 2
#         if N == 1:
#             result.append(1)
#             state = True
#             break
#         if N > 1:
#             N -= 1
#             result.append(1)
#         else:
#             result.append(0)
#         cnt += 1
#     if state:
#         print(f'#{tc}',end = ' ')
#         print(*result, sep='')
#     else:
#         print(f'#{tc} overflow')
#


####
# for t in range(1, int(input())+1):
#     a = float(input())
#     res = ''
#     int_to_bin = 1
#     while True:
#         a *= 2
#         if a >= int_to_bin:
#             a-=int_to_bin
#             res += str(1)
#         else:
#             res += str(0)
#         if a == 0:
#             break
#         if len(res) >= 13:
#             res = 'overflow'
#             break
#     print(f'#{t} {res}')



for t in range(int(input())):
    lst = list(input().split())

    ans = bin(int('0x' + lst[1], 16)).replace('0b','0')
    if int(lst[0]) * 4 == len(str(ans)):
        print(f"#{t + 1} {ans}")
    else:
        awr = bin(int('0x' + lst[1], 16))
        while len(str(awr)) < 4:
            awr = '0' + str(awr)
        print(f"#{t + 1} {awr[2:]}")

# T = int(input())
# for tc in range(1, T + 1):
#     n, hex_n = input().split()
#     hex_n=bin(int(hex_n,16))
#     hex_n=str(hex_n)[2:]
#     if n*4 == len(hex_n):
#         print(f'#{tc} {hex_n}')
#     else:
#         print(f'#{tc} {"0" * ((int(n)*4)-len(hex_n))+hex_n}')