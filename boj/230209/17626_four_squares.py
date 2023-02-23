num = int(input())

dic = {}

for i in range(1, 225):
    dic[i] = i**2

# print(dic)

# 1,2, 3,   1, 2, 3, 4, 2,  1, 2, 3, 4, 2, 3, 4,  1,2,3,4, 2, 3,4,2 3
cnt = 1

for i in range(1, len(dic.keys())+1):
    if num in dic.values():
        print(cnt)
        break

    # print(dic.get(i))


    if num > dic.get(i):
        print(num)
        for j in range(4):
            cnt += j
            a = dic.get(i) + j
            if a == dic:
                print(cnt)
            else:
                cnt = 1

