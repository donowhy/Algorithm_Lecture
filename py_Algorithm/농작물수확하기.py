for t in range(int(input())):
    num = int(input())
    lst = [list(input()) for _ in range(num)]
    ans = []
    k = 0
    for i in range(num):
        if i < num // 2 + 1 :
            for j in range( -i , i + 1):
                ans.append(int(lst[i][num // 2 + j]))
        else:
            k += 1
            for j in range( i - num//2 , num - k):
                ans.append(int(lst[i][j]))

    print(f'#{t+ 1} {sum(ans)}')

# 민승짱 화이팅 ~ !