# https://www.acmicpc.net/problem/10818

import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split(' ')))

min_num = min(num_list)
max_num = max(num_list)

print(f'{min_num} {max_num}')
