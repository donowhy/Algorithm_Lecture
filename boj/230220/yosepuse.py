a, b = map(int,input().split())

stk = []
arr = []
for i in range(1,a+1):
    stk.append(i)

while len(stk) >= 1:
    for i in range(b-1):
        stk.append(stk.pop(0))
    arr.append(stk.pop(0))

print("<".rstrip(),', '.join(list(map(str,arr))),">".strip())




from collections import deque

n, k = map(int, input().split())

# 1~n번 사람
people = deque()
for i in range(1, n+1): people.append(i)
result = []

while people:
  for _ in range(k-1):
    people.append(people.popleft())

  result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))