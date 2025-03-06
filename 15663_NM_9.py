import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
visited = [0] * N
s = []

def dfs():
    check_num = 0

    if len(s) == M:
        print(" ".join(map(str,s)))
        return
    
    for i in range(N):            
        if check_num != arr[i] and visited[i]==0:
            s.append(arr[i])
            visited[i] = 1
            check_num = arr[i]
            dfs()
            visited[i] = 0
            s.pop()
dfs()
