import sys
input = sys.stdin.readline()
sys.stdin = open('input.txt', 'r')

def max_index(lst):
    mx = lst[0]
    mx_idx = 0
    for i in lst:
        if mx < lst[i]:
            mx = lst[i]
            mx_idx = i
    return mx_idx
def min_index(lst):
    mn = lst[0]
    mn_idx = 0
    for i in lst:
        if mn < lst[i]:
            mn = lst[i]
            mn_idx = i
    return mn_idx


for tc in range(1, 11):
#    #입력
    c = int(input()) #덤프 횟수
    boxes = list(map(int, input().split())) #상자들의 높이 리스트

# 처리
# for i : [0, 덤프횟수)
    for i in range(c):
#    # 최댓값이 있는 상자 리스트의 인덱스를 찾는다.
        mx_idx = max_index(boxes)
#    # 최솟값이 있는 상자 리스트의 인덱스를 찾는다.
        mn_idx = min_index(boxes)
#    # 최댓값 -1, 최솟값 +1
        boxes[mx_idx] -= 1
        boxes[mn_idx] += 1

#출력
#최댓값을 찾고, 최솟값을 찾고, 이 값의 차를 출력
    print(f'#{tc} {max(boxes) - min(boxes)}')

#방법 2
for tc in range(1, 11):
#    #입력
    c = int(input()) #덤프 횟수
    boxes = list(map(int, input().split())) #상자들의 높이 리스트

#로직
# 박스 리스트 정렬 (오름차순)
    boxes.sort()
    # 왼쪽에는 최솟값, 오른쪽에는 최댓값
    # boxes[0], boxes[-1]

    for i in range(c):
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()

    print(f'#{tc} {boxes[-1] - boxes[0]}')