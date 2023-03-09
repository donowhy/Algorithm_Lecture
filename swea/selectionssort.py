# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(N-1): # 주어진(작업) 구간의 시작인덱스
#     minIdx = i      # 맨 앞이 최소라 가정
#     for j in range(i + 1, N):
#         if arr[minIdx] > arr[j]:
#             minIdx = j
#         arr[minIdx], arr[i] = arr[i], arr[minIdx]
# print(arr)

#잘못된 방법
# def SelectionSort():
#     n = int(input())
#     arr = list(map(int,input().split()))
#     for i in range(n-1):
#         mini = i
#         for j in range(i+1,n):
#             if arr[mini] > arr[j]:
#                 mini = j
#             arr[mini], arr[i] = arr[i], arr[mini]
#
#     return arr
#
# print(SelectionSort())

#옳은 방법
arr = [67, 39, 16, 49, 60, 28, 8 ,85 ,89, 11]
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(selection_sort(arr))