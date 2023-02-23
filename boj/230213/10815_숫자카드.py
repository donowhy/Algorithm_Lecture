import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

T = int(input())
lst = list(map(int, input().split()))

for i in range(len(lst)):

    if lst[i] in arr:
        print(1)
    else:
        print(0)



#이진탐색
import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
checks = list(map(int, input().split()))

for check in checks:
    low, high = 0, N-1  # cards의 이진 탐색 index
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] > check:  # 중간 값보다 작다면
            high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
        elif cards[mid] < check:  # 중간 값보다 크다면
            low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')

#딕셔너리
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

_dict = {}  # 속도는 dictionary!
for i in range(len(cards)):
    _dict[cards[i]] = 0  # 아무 숫자로 mapping

for j in range(M):
    if checks[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')