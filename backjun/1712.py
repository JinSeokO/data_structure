# https://www.acmicpc.net/problem/1712

import sys

A, B, C = map(int, sys.stdin.readline().split(' '))

profit = C - B

# while 문으로 + - 로 할 경우 런타임 에러
if profit <= 0:
    print(-1)
else:
    cnt = A // profit + 1
    print(cnt)
