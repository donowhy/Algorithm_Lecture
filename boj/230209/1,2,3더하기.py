N = int(input())

num_lst = []
dp_lst = {}

for i in range(N):
    M = int(input())
    num_lst.append(M)

dp_lst[1]=1
dp_lst[2]=2
dp_lst[3]=4

for num in range(4, 12):
    result = dp_lst[num-3] + dp_lst[num-2] + dp_lst[num-1]
    dp_lst[num] = result


for i in num_lst:
    print(dp_lst.get(i))

