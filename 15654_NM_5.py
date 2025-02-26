import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

s = []

def dfs(start):
    if len(s)==M:
        print(' '.join(map(str,s)))
        return

    for i in arr:
        if i in s:
            continue
        s.append(i)
        dfs(i)
        s.pop()

dfs(min(arr))

