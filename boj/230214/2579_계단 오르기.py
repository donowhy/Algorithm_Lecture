n=int(input())
s=[int(input()) for _ in range(n)]
print(s, 's입력')
dp=[0]*(n)
if len(s)<=2:
    print(sum(s), 'sum(s)')
else:
    dp[0]=s[0]
    dp[1]=s[0]+s[1]
    for i in range(2,n):
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
        print(dp[i], 'dp')
        print(dp, 'dp전체 리스트')
    print(dp[-1])