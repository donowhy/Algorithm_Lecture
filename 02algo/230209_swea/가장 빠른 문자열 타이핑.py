# tc = int(input())
#
# for i in range(tc):
#     string,letter = map(str,input().split())
#     cnt = 0
#     k = 0
#     for j in range(len(string)):
#         if (string[j+k : j + len(letter)+ k + 1] == letter):
#             if j + len(letter) + k >= len(string):
#                 break
#             else:
#                 print(string[j+k : j + len(letter)+k])
#                 cnt += 1
#                 print(cnt)
#                 if True:
#                     k += j- 1
#
#     # print(cnt)
#
#     # print(len(string))
#     ct = (len(string) - (cnt * len(letter))) + cnt
#     print(f'#{i+1} {ct}')


# 방법 1
def pt_count(pat, txt):
    return txt.count(pat)


T = int(input())

for test_case in range(1, T + 1):
    A, B = map(str, input().split())

    cnt = 0
    for _ in range(len(A)):
        cnt += 1

    cnt = cnt - pt_count(B, A) * len(B) + pt_count(B, A)

    print(f'#{test_case} {cnt}')


#방법 2
def BruteForce(pat, txt):
    N, M = len(txt), len(pat)
    i = j = 0
    pat_cnt, cnt = 0, 0

    while j < M and i < N:
        if txt[i] != pat[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == M:
            pat_cnt += 1
            j = 0

    return pat_cnt

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(str, input().split())
    cnt = 0

    for i in range(len(A)):
        cnt += 1

    cnt = cnt - BruteForce(B, A) * len(B) + BruteForce(B, A)

    print(f'#{test_case} {cnt}')

'''



9
baaaa aaa
asaaaaaa aaa
aaaaa aa
ababa aba
banana bana
asakusa sa
osaca sa
oriental tal
kkkkk k
 '''