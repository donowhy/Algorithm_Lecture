import pprint

'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''



N = int(input())

for i in range(N):
    M = int(input())
    lst = [[0] * 10 for _ in range(10)]
    for j in range(M):
        lst_input = list(map(int,input().split()))

        if lst_input[-1] == 1:
            for k in range(lst_input[0], lst_input[2]+1):
                for l in range(lst_input[1], lst_input[3]+1):
                    lst[k][l] += 1
        else:
            for k in range(lst_input[0], lst_input[2]+1):
                for l in range(lst_input[1], lst_input[3]+1):
                    lst[k][l] += 1


        hap = 0
        for m in range(10):
            for n in range(10):
               if lst[m][n] == 2:
                   hap +=1

    print(f'#{i + 1} {hap}')
