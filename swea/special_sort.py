import pprint

N = int(input())

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


for i in range(1, N+1):
    M = int(input())
    arr = list(map(int, input().split()))

    for j in range(len(arr) - 1):
        min_idx = j
        for l in range(j + 1, len(arr)):
            if arr[l] < arr[min_idx]:
                min_idx = l
        arr[j], arr[min_idx] = arr[min_idx], arr[j]
    print(arr)
    lst = []
    for k in range(1, 11):
        if k % 2:
            lst.append(arr.pop(-1))
        else:
            lst.append(arr.pop(0))

    print(f'#{i}', *lst)

    #
    # print(f'#{i} ',end='')
    # for z in range(10):
    #     print(lst[z],end=' ')
    # print()
