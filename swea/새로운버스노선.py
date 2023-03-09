# 1 일반, 2 급행, 3광역급행
# A, B가 빈칸으로 구분되어 주어진다.
# 1, 은 모든 정류장에 정차
# 2, 급행, A가 짝수면 짝수번호에 정차, 홀수면 홀수번호에 정차
# 3, 광역, A가 짝수면 A와 B사이의 모든 4의 배수 정류장
# A가 홀수인 경우 A와 B사이의 3의 배수면서 10의 배수가 아닌 정류장

# T, N, 타입, A,B

# 1 은 B - A - 1  로 반환
# 2 조건문으로 2로 나눴을 때 나머지가 있을경우와 없을 경우를 카운트
# 3 배수 또한 나머지가 0 일때 + 10의 배수가 아닌 건 != 로 풀기
# 최대 같은 정류장 몇 개?

from collections import Counter

T = int(input())
for z in range(1,T+1):
    N = int(input())

    lst = []
    lst_count = {}
    cnt = 0
    for tc in range(N):
        a, b, c = map(int, input().split())
        lst.append(b)
        lst.append(c)
        if a == 1:
            for stop in range(b + 1, c):
                lst.append(stop)

        elif a == 2:
            if b % 2 == 0:
                for stop in range(b + 1, c):
                    if stop % 2 == 0:
                        lst.append(stop)
            else:
                for stop in range(b + 1, c):
                    if stop % 2:
                        lst.append(stop)

        else:
            if b % 2 == 0:
                for stop in range(b + 1, c):
                    if stop % 4 == 0:
                        lst.append(stop)
            else:
                for stop in range(b + 1, c):
                    if stop % 3 == 0:
                        if not stop % 10 == 0:
                            lst.append(stop)

        lst.sort()
        # print(lst)
        lst_count = Counter(lst)
        # print(lst_count)
        # print(max(lst_count.values()))
    print(f'#{z} {max(lst_count.values())}')
