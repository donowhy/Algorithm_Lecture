N, K = map(int, input().split())

cnt = 0
sm = 0

for _ in range(N):
    S, Y = map(int, input().split())
    if Y == 1:
        hap = 0
        if S == 0:
            hap += 1
            if hap % 2 == 0:
                cnt += int(hap // 2)
            else:
                cnt += int(hap // 2 + 1)

        else:
            sm += 1
            if sm % 2 == 0:
                cnt += int(sm // 2)
            else:
                cnt += int(sm // 2 + 1)

    if Y == 2:
        hap = 0
        if S == 0:
            hap += 1
            if hap % 2 == 0:
                cnt += int(hap // 2)
            else:
                cnt += int(hap // 2 + 1)

        else:
            sm += 1
            if sm % 2 == 0:
                cnt += int(sm // 2)
            else:
                cnt += int(sm // 2 + 1)

    if Y == 3:
        hap = 0
        if S == 0:
            hap += 1
            if hap % 2 == 0:
                cnt += int(hap // 2)
            else:
                cnt += int(hap // 2 + 1)

        else:
            sm += 1
            if sm % 2 == 0:
                cnt += int(sm // 2)
            else:
                cnt += int(sm // 2 + 1)

    if Y == 4:
        hap = 0
        if S == 0:
            hap += 1
            if hap % 2 == 0:
                cnt += int(hap // 2)
            else:
                cnt += int(hap // 2 + 1)

        else:
            sm += 1
            if sm % 2 == 0:
                cnt += int(sm // 2)
            else:
                cnt += int(sm // 2 + 1)

    if Y == 5:
        hap = 0
        if S == 0:
            hap += 1
            if hap % 2 == 0:
                cnt += int(hap // 2)
            else:
                cnt += int(hap // 2 + 1)

        else:
            sm += 1
            if sm % 2 == 0:
                cnt += int(sm // 2)
            else:
                cnt += int(sm // 2 + 1)


    if Y == 6:
        hap = 0
        if S == 0:
            hap += 1
            if hap % 2 == 0:
                cnt += int(hap // 2)
            else:
                cnt += int(hap // 2 + 1)

        else:
            sm += 1
            if sm % 2 == 0:
                cnt += int(sm // 2)
            else:
                cnt += int(sm // 2 + 1)

print(cnt)