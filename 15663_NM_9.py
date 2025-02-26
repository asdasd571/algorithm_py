import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = list(map(int,input().split()))
arr_set = set(arr)
arr_set = sorted(arr_set)
s = []

def dfs(start):
    if len(s)==M:
        print(' '.join(map(str,s)))
        return

    for i in arr_set:
        
        s.append(i)
        dfs(i)
        s.pop()

dfs(min(arr_set))

