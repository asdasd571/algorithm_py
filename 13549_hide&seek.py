import sys
from collections import deque

input = sys.stdin.readline
MAX = 10**5
visited = [0] * (MAX+1)
def bfs(x,y):
    queue = deque([x])
    visited[x] = 1
    while queue:
        
        x = queue.popleft()
        if x == y:
            return
        for nx in (2*x,x-1,x+1):
            if nx < 0 or nx > MAX:
                continue
            if visited[nx]:
                continue

            if nx==2*x:
                visited[nx] = visited[x]
            
            else:
                visited[nx] = visited[x] + 1
            queue.append(nx)

N,K = map(int,input().split())

bfs(N,K)
print(visited[K]-1)