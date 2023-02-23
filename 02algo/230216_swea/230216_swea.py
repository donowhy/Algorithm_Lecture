# 모든 부분집합 구하기

def DFS(v):
    if v == n + 1:
        print(ch)
        print()
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()

    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    DFS(1)


#부분집합 합 구하기
def solve(ar, n, x):
    if x == 0:
        return True
    if n == 0:
        return False
    if ar[0] > x:
        return solve(ar[1:], n - 1, x)

    return solve(ar[1:], n - 1, x) or solve(ar[1:], n - 1, x - ar[0])


if __name__ == '__main__':
    ar = list(map(int, input().split()))
    n = len(ar)
    x = int(input())
    print(solve(ar, n, x))