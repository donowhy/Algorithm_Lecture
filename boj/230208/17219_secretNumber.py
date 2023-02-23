import pprint

N, M = map(int,input().split())
arr = []
lst = []
for _ in range(N):
    sites = input().split()
    lst.append(sites)
print(lst)

for _ in range(M):
    wnt = input().split()
    arr.append(wnt)



for i in range(len(arr)):

    print(arr[i])
    for j in range(len(lst)):
        if arr[i] == lst[j][0]:
            print(1111)

        연습연습연습
