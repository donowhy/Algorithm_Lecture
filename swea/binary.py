'''
9
400 300 350
999 299 578
888 222 888
400 300 350
1000 299 578
1000 222 888
123 64 12
912 912 99
100 54 100
 '''
N = int(input())

for i in range(N):
    p,a,b = map(int,input().split())
    cnt = 0
    low = 1
    high = p
    mid = (low + high) // 2

    while True:
        cnt += 1

        if mid < a:
            low = mid
            mid = (low + high) // 2

        elif mid > a:
            high = mid
            mid = (low + high) // 2

        elif mid == a:
            break

    count = 0
    low = 1
    high = p
    mid = (low + high) // 2

    while True:
        count += 1

        if mid < b:
            low = mid
            mid = (low + high) // 2
        elif mid > b:
            high = mid
            mid = (low + high) // 2
        elif mid == b:
            break

    if cnt > count:
        print(f'#{i+1} B')
    elif cnt < count:
        print(f'#{i+1} A')
    else:
        print(f'#{i+1} 0')

'''
N = int(input())

for i in range(N):
    p,a,b = map(int,input().split())
    cnt = 0
    count = 0
    low = 1
    high = p
    mid = (high + low) // 2

    while True:
        cnt += 1

        if mid < a:
            low = mid + 1
            mid = (high + low) // 2

        elif mid > a:
            high = mid - 1
            mid = (high + low) // 2

        else:
            mid == a
            break

    count = 0
    low = 1
    high = p
    mid = (high + low) // 2

    while True:
        count += 1

        if mid < b:
            low = mid + 1
            mid = (high + low) // 2
        elif mid > b:
            high = mid - 1
            mid = (high + low) // 2
        else:
            mid == b
            break

    if cnt > count:
        print(f'#{i+1} B')
    elif cnt < count:
        print(f'#{i+1} A')
    else:
        print(f'#{i+1} 0')
'''