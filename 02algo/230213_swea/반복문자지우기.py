#
# def check(string):
#     global stack
#
#     for ch in string:
#         try:
#             if ch == string[0]:
#                 stack.append(string[0])
#             elif ch == ')':
#                 if stack.pop() == '(':
#                     continue
#                 return False
#             elif ch == '{':
#                 stack.append('{')
#             elif ch == '}':
#                 if stack.pop() == '{':
#                     continue
#                 return False
#
#         except:
#             return False
#
#     if len(stack) == 0:
#         return True
#     return False




T = int(input())

while 1:
    for j in range(1, T+1):
        stack = []

        string = input()
        for i in range(len(string)):
            if string[i] == string[i+1]:
                string = string[0:i] + string[i+2:]


            if len(string) == 0:
                break
            else:
                print(string)
                break