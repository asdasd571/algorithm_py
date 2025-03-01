import sys
input = sys.stdin.readline

N = int(input())

score = list(map(int,input().split()))
max_dp = score 
min_dp = score 
for _ in range(N-1):
    score = list(map(int,input().split()))

    max_dp = [score[0] + max(max_dp[0],max_dp[1]), score[1] + max(max_dp), score[2] + max(max_dp[1],max_dp[2])]
    min_dp = [score[0] + min(min_dp[0],min_dp[1]), score[1] + min(min_dp), score[2] + min(min_dp[1],min_dp[2])]

print(max(max_dp),min(min_dp))