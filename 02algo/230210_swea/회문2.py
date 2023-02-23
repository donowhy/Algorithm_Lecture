# 가로 회문 검사
def checking_c():
    global count

    for K in range(100, 0, -1):  # 가장 큰 개수인 100개 부터 ~ 1개 까지 뽑아주며 검사
        for i in range(100):
            for j in range(100):
                if j + K > 100:  # 만약 K를 뽑을 수 없다면
                    break  # 반복문 탈출후 다음 행으로 넘어간다.
                e = j + K - 1  # 끝 인덱스를 설정
                for h in range(j, j + (K // 2)):  # 절반을 돌면서
                    if word[i][h] != word[i][e]:  # 양쪽에서 안으로 들어오면서 검사하는데 만약 다르다면
                        break  # 반복문탈출
                    e -= 1  # 끝쪽 인덱스를 -1씩 해준다.
                else:  # 반복문을 다돌았다면 회문이므로
                    count = K  # 그 길이를 설정 후
                    return  # 함수 탈출


# 세로 회문 검사
def checking_r():
    global count

    for K in range(100, 0, -1):  # 가장 큰 개수인 100개 부터 ~ 1개 까지 뽑아주며 검사
        if count >= K:  # 만약 가로에서 뽑은 회문 길이보다 이미 뽑을 K개가 더 작아졌다면 더이상 의미없으므로
            return  # 함수 리턴
        for i in range(100):
            if i + K > 100:  # 만약 K개를 뽑을 수 없다면
                break  # 반복문 탈출
            for j in range(100):
                e = i + K - 1  # 끝 인덱스 설정
                for h in range(i, i + (K // 2)):  # 절반을 나누어 양쪽 끝에서 안으로 들어면서 검사
                    if word[h][j] != word[e][j]:  # 만약 대칭을 기준으로 글자가 다르다면
                        break  # 반복문탈출
                    e -= 1  # 끝 인덱스를 -1씩 해준다.
                else:  # 반복문을 다돌았다면 회문이므로
                    count = K  # 그 개수를 K로 저장 후
                    return  # 탈출


for _ in range(1, 10 + 1):
    order = int(input())
    word = [list(map(str, input())) for _ in range(100)]

    count = 0
    # 가로 검사
    checking_c()

    # 세로 검사
    checking_r()

    print(f'#{order} {count}')

#방법 2
def check(a):
    l = len(a)
    for i in range(l // 2):
        if a[i] != a[l - i - 1]:
            return False
    return True

T = 10
for t in range(1, T + 1):
    input()
    length = 100
    map_list = []
    map_list2 = []
    N = 100
    for i in range(N):
        map_list.append(input())
    for i in range(N):
        str_temp = ''
        for k in range(N):
            str_temp += map_list[k][i]
        map_list2.append(str_temp)
    result = 0
    for t_len in range(length, 0, -1):
        if result >= t_len:
            break
        for i in range(N):
            if result == t_len:
                break
            for j in range(N - t_len + 1):
                if check(map_list[i][j:j + t_len]) or check(map_list2[i][j:j + t_len]):
                    result = t_len
                    break

    print("#{} {}".format(t, result))

    '''

1
CCBBC
ACBAA
CCCAC
CABAC
BCCBC
    
    '''

