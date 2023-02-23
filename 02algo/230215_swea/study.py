'''

# 부분 집합 만들기
# i는 현재 해당되는 인덱스의 값을 0 또는 1로 바꿔주는 값
# k값은 인덱스의 끝, 배열의 크기 (기저조건)
# count 라는 매개변수
def f1(i, k, count):
    if i == k: # 기저조건
        if count == 2:
            for idx, bit in enumerate(bits):
                if bit:
                    print(A[idx], end=', ')
            print()
        return
    # i에 해당되는 인덱스 값을 0 으로 바꿔준다 (그 후에 재귀호출 -> 다음 i+1)
    bits[i] = 0
    f1(i+1, k, count)
    # i에 해당되는 인덱스 값을 1 으로 바꿔준다
    bits[i] = 1
    f1(i+1, k, count+1)

A = [1, 2, 3, 4]
N = len(A)
bits = [0] * N
f1(0, N, 0)

'''

def f1(i, k, tot):
    if tot > 10:
        return
    if i == k:  # 기저조건
        if tot == 10:
            for idx in range(k):
                if bits[idx]:
                    print(A[idx], end = ' ')
            print()
        return

        # tot = 0
        # for idx, bit in enumerate(bits):
        #     if bit == 1:
        #        tot += A[idx]
        # if  tot == 10:
        #     print(bits)
        #     for idx, bit in enumerate(bits):
        #         if bit:
        #             print(A[idx], end=' ')
        #     print()
        return
    # i에 해당되는 인덱스 값을 0 으로 바꿔준다 (그 후에 재귀호출 -> 다음 i+1)
    bits[i] = 0
    f1(i + 1, k, tot)
    # i에 해당되는 인덱스 값을 1 으로 바꿔준다
    bits[i] = 1
    f1(i + 1, k, tot)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
bits = [0] * N
f1(0, N, 0)
