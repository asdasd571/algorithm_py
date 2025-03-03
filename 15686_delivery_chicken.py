import sys
input = sys.stdin.readline
ans = 999999999
N,M = map(int,input().split())

home = []
chick = []

for i in range(N):
    row = list(map(int,input().split()))
    
    for j in range(N):
        if row[j] == 1:
            home.append((i,j))
        elif row[j] == 2:
            chick.append((i,j))
visited = [0] * len(chick)

def dfs(idx,cnt):
    global ans

    if cnt == M:
        min_ans = 0

        for i in home:
            dist = 999999999
            for j in range(len(visited)):
                if visited[j]:
                    check_num = abs(i[0]-chick[j][0]) + abs(i[1]-chick[j][1])
                    dist = min(dist,check_num)
            min_ans += dist

        ans = min(ans,min_ans)

        return
    
    for i in range(idx,len(chick)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,cnt+1)
            visited[i] = 0

dfs(0,0)
print(ans)
