tc = int(input())

for i in range(1, tc + 1):
    bckth = list(map(str,input().split()))
    stk = []
    num = 0
    pls = 0
    for j in range(len(bckth)):
        try:
            if int(bckth[j]) > 0:
                num += 1

            elif int(bckth[j]) <= 0:
                num += 1

        except:
            if bckth[j] != '.':
                pls += 1

    for j in range(len(bckth)):
        if num == pls + 1:
            try:
                if int(bckth[j]) > 0:
                    stk.append(bckth[j])
                elif int(bckth[j]) <= 0:
                    stk.append(bckth[j])
            except:
                if len(stk) >= 2:
                    a = int(stk.pop())
                    b = int(stk.pop())
                    if bckth[j] == '+':
                            c = b + a
                            stk.append(c)

                    elif bckth[j] == '-':
                            c = b - a
                            stk.append(c)

                    elif bckth[j] == '*':
                            c = b * a
                            stk.append(c)
d
                    elif bckth[j] == '/':
                            c = int(b/a)
                            stk.append(c)

                elif len(stk) == 1:
                    result = int(stk.pop())
                    print(f'#{i} {result}')

        else:
            print(f'#{i} error')
            break
#
'''
4
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
6 5 2 8 - * 2 / + .

1
6 5 2 8 - * 2 / + .
'''

#후위 연산자
# 중위 표현식 입력
string = input()

# 스택
result = []
stack = []
for ch in string:
    # 1. 피연산자 (숫자이면)
    if ch.isnumeric():
        result.append(ch)
    # 2. '(' 라면
    elif ch == '(':
        stack.append(ch)
    # 3. '*', '/' 라면
    elif ch == '*' or ch == '/': # elif ch in ['*', '/']:
        # 만약에 top에 이미 '*', '/' 있다면 얘네는 pop 해준다.
        if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/'):
            a = stack.pop()
            result.append(a)
        # 그리고 자기 자신은 stack 에 추가
        stack.append(ch)
    # 4. '+', '-' 라면
    elif ch == '+' or ch == '-':
        # 기존에 stack에 들어있던 값이 우선순위가 높다면 빼준다
        while len(stack) > 0 and stack[-1] in ['+', '-', '*', '/']:
            a = stack.pop()
            result.append(a)
        stack.append(ch)
    # 5. ')' 라면
    elif ch == ')': # else:
        # 여는 괄호가 나올 때까지 pop을 해준다
        while stack[-1] != '(':
            a = stack.pop()
            result.append(a)
        stack.pop() # '('


# stack 에 남아있는 연산자들을 모두 빼준다
while len(stack) > 0:
    a = stack.pop()
    result.append(a)


print(*result)



