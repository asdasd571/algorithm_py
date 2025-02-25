import sys
import heapq

N = int(input())
M = int(input())

graph = [[] for i in range(N+1)]
dist = [1e9 for _ in range(N+1)]

for _ in range(M):
    s,f,c = map(int,input().split())
    graph[s].append([f,c])



start,end = map(int,input().split())
heap = []
heapq.heappush(heap,[0,start])
dist[start] = 0

cost = 0

while heap:
    cur_c, cur_v = heapq.heappop(heap)
    if dist[cur_v] < cur_c:
        continue 
    
    for next_v, next_c in graph[cur_v]:
        sum_cost = cur_c + next_c
        if sum_cost >= dist[next_v]:
            continue
        
        dist[next_v] = sum_cost
        heapq.heappush(heap,[sum_cost,next_v])

print(dist[end])