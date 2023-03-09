t = int(input())

for tc in range(1, t + 1):
    lst = [list(input()) for _ in range(5)]
    arr = []
    ans = []
    for long in range(len(lst)):
        arr.append(len(lst[long]))

    for i in range(max(arr)):
        for j in range(len(lst)):
            try:
                ans.append(lst[j][i])
            except:
                continue

    print(f"#{tc} {''.join(ans)}")