import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

heap = []  # 우선순위 큐는 빈 리스트로 초기화
graph = [[] for _ in range(V+1)]  # 올바른 인접 리스트 초기화
dist = [1e9] * (V+1)  # 거리 배열 크기 수정 (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 올바르게 간선 추가

heapq.heappush(heap, (0, K))  # (가중치, 정점) 순서로 저장
dist[K] = 0

while heap:
    cur_w, cur_v = heapq.heappop(heap)
    
    if dist[cur_v] < cur_w:
        continue
    
    for next_v, next_w in graph[cur_v]:
        sum_w = cur_w + next_w
        if sum_w < dist[next_v]:
            dist[next_v] = sum_w
            heapq.heappush(heap, (sum_w, next_v))  # (가중치, 정점) 순서 유지

for i in range(1, V+1):  # 1번부터 V번까지 출력
    print("INF" if dist[i] == 1e9 else dist[i])

'''
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
'''