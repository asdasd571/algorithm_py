import sys
input = sys.stdin.readline

N,M = map(int,input().split())

know_list = set(map(int,input().split()[1:]))
parties = []
for _ in range(M):
    parties.append(set(map(int,input().split()[1:])))

for _ in range(M):
    for party in parties:
        if party & know_list:
            know_list = know_list.union(party)
cnt = 0
for party in parties:
    if party & know_list:
        continue
    cnt+=1

print(cnt)