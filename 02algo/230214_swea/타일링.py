tc = int(input())

for i in range(1, tc + 1):
    dp = [0] * 301
    n = int(input())

    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    for j in range(4,301):
        dp[j] = (dp[j - 1] + dp[j - 2]*2)

    print(f'#{i} {dp[n//10]}')