from itertools import combinations

tc = int(input())


lst = []
dic = {}

for i in range(tc):
    num = int(input())
    for j in range(num):
        wear = list(map(str, input().split()))
        lst.append(wear)

for j in range(len(lst)):
    if lst[j][1] != 'face':
        combi = list(combinations(lst[j],2))
        combi_1 = list(combinations(lst[j],1))

print(combi)
print(combi_1)




    # for k in range(len(lst)):
    #    dic[lst[k][1]] = lst[k][0]


# print(dic)
# print(dic)


"""
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
"""


#방법 2 딕셔너리와 Counter 모듈을 활용한 풀이
import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = []

    n = int(input())
    for _ in range(n):
        k = input().split()[1]
        clothes.append(k)
    clothes = Counter(clothes)

    # 아무 의류도 없으면 0, 의류 종류 수가 1이라면, 그 의류 수만큼이 답인데 그게 저 구문에 다 포함됨
    # 의류 종류가 둘 이상이라면, (어떤 의류 종류의 의류 수+1)를 모든 종류에 대해
    # 서로 곱해주고, 1을 빼준다. 저 괄호에서 +1이 있는 이유는 그 종류의 의류를
    # 입지 않는 경우를 포함한 것이고, 다 계산 후 마지막에 1을 빼는 이유는
    # 모든 의류를 하나도 입지 않는 경우를 제외하기 위함이다.
    count = 1
    for key in clothes.keys():
        count *= clothes[key] + 1
    print(count - 1)


#방법 3 딕셔너리
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = {}

    n = int(input())
    for _ in range(n):
        v, k = input().split()
        # 의류 종류가 dict에 없다면 새로 넣어주고, 아니면 원래 있던 의류 종류 키에 대해,
        # set 밸류에 v 추가해주기
        if clothes.get(k) == None:
            clothes[k] = set()
        clothes[k].add(v)

    # 아무 의류도 없으면 0, 의류 종류 수가 1이라면, 그 의류 수만큼이 답인데 그게 저 구문에 다 포함됨
    # 의류 종류가 둘 이상이라면, (어떤 의류 종류의 의류 수+1)를 모든 종류에 대해
    # 서로 곱해주고, 1을 빼준다. 저 괄호에서 +1이 있는 이유는 그 종류의 의류를
    # 입지 않는 경우를 포함한 것이고, 다 계산 후 마지막에 1을 빼는 이유는
    # 모든 의류를 하나도 입지 않는 경우를 제외하기 위함이다.
    count = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1
    print(count - 1)