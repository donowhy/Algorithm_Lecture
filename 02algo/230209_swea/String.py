for i in range(10):
    tc = int(input())
    letter = input()
    string = input()
    cnt = 0

    for j in range(len(string)-1):
        if string[j:j+len(letter)] == letter:
            cnt += 1

    print(f'#{i+1} {cnt}')