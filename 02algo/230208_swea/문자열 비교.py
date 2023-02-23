import sys
sys.stdin = open('input_munja.txt', 'r')

tc = int(input()) # 테스트 케이스

for j in range(tc):
    txt = input() #문자열 1
    tst= input()  #문자열 2

    if txt in tst:  #문자열 2 안에 문자열 1이 있으면 True
        print(f'#{j+1} 1')
    else:
        print(f'#{j+1} 0')