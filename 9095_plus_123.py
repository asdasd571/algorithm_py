import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)

    for i in range(1,N+1):
        if i==1:
            dp[i] = 1
        elif i==2:
            dp[i] = 2
        elif i==3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])


'''
4를 1,2,3의 합으로 나타내는 법은
3 + 1을 나타내는 경우의 수 
2 + 2를 나타내는 경우의 수
1 + 3을 나타내는 경우의 수
를 다 더한 값?
'''