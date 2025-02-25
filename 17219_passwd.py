import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dict = {}

for i in range(N):
    site,passwd = map(str,input().split())
    site = site.rstrip()
    dict[site] = passwd

for i in range(M):
    sites = input().rstrip()
    print(dict[sites])