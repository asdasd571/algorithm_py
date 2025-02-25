import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dict = {}

for i in range(1,N+1):
    target = input().rstrip()
    dict[target] = i
    dict[i] = target

for i in range(M):
    targets = input().rstrip()
    if targets.isdigit():
        print(dict[int(targets)])
    else:
        print(dict[targets])