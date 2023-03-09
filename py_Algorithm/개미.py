# import sys
# input = sys.stdin.readline
#
# a, b = map(int,input().split())
# x, y = map(int,input().split())
# t = int(input())
#
# while t > 0:
#     x += 1
#     y += 1
#     t -= 1
#
# x = abs(x - (x - a) * 2)
# while a <= x:
#     x -= a
#
# while b <= y:
#     y = abs(y - (y - b) * 2)
#
# print(x, y)

#
# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
#
# a = (p + t) // w  # 증가하는 부분인지 감소하는 부분인지 확인
# b = (q + t) // h  # 증가하는 부분인지 감소하는 부분인지 확인
# print(a, b)
# if a % 2 == 0:  # 해당 값이 증가하는 부분이라면
#     x = (p + t) % w
#     print(x, '증가')
# else:  # 해당 값이 감소하는 부분이라면
#     x = w - (p + t) % w
#     print(x, '감소')
# if b % 2 == 0:  # 해당 값이 증가하는 부분이라면
#     y = (q + t) % h
#     print(y, '증가')
# else:  # 해당 값이 감소하는 부분이라면
#     y = h - (q + t) % h
#     print(y, '감소')
#
# print(x, y)


print(divmod(6, 4))

def func(n, l):
    global t
    s, r = divmod(n+t, l)
    pos = l - r if s % 2 else r
    return pos


w, h = map(int, input().split())    # 가로, 세로
p, q = map(int, input().split())
t = int(input())
print(func(p, w), func(q, h))
#
#
#
#
# w, h = map(int, input().split())
# x, y = map(int, input().split())
# t = int(input())
# print(w - abs(w-(x+t)%(2*w)), h - abs(h-(y+t)%(2*h)))
#
#
#
#
# import sys
# input = sys.stdin.readline
#
# garo, sero = map(int, input().split())
# x, y = map(int, input().split())
# t = int(input())
#
# x = x + t
# y = y + t
#
# if (x//garo) % 2 == 0:
#     x = x % garo
# else :
#     x = garo - (x%garo)
#
# if (y//sero) % 2 == 0:
#     y = y % sero
# else :
#     y = sero - (y % sero)
#
# print(x, y)