import sys
input = sys.stdin.readline

N = int(input())
stair = [int(input()) for _ in range(N)]

if N == 1:  # 계단이 하나일 경우
    print(stair[0])
    exit()
elif N == 2:  # 계단이 두 개일 경우
    print(stair[0] + stair[1])
    exit()

dp = [0] * N

# 초기 값 설정
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])  # i=2일 때는 i-3이 없음

for i in range(3, N):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[-1])  # 마지막 계단을 밟는 최댓값 출력



'''
🚀 문제 핵심 정리
한 번에 한 계단 or 두 계단씩 오를 수 있음
연속된 세 개의 계단을 연속해서 밟을 수 없음
마지막 계단은 반드시 밟아야 함
즉, 최댓값을 구하기 위해서 마지막 계단을 밟으면서도 규칙을 지켜야 해!

🔍 dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
이제 이 점화식을 해석해보자.
우리는 **"i번째 계단을 밟을 때, 최대 점수"**를 구하고 싶어.

✅ 첫 번째 경우: dp[i-3] + stair[i-1] + stair[i]

i번째 계단을 밟기 직전에 (i-1)번째 계단을 밟았다고 가정
하지만 연속 3개 계단을 밟을 수 없으므로 (i-2)번째 계단은 건너뛴 상태여야 함
즉, (i-3)번째 계단까지의 최대 점수 + (i-1)번째 계단 점수 + (i번째 계단 점수)
✅ 두 번째 경우: dp[i-2] + stair[i]

i번째 계단을 밟기 직전에 (i-1)번째 계단을 건너뛰고 i-2번째 계단에서 바로 올라온 경우
즉, (i-2)번째 계단까지의 최대 점수 + (i번째 계단 점수)
💡 두 가지 방법 중 더 큰 값을 선택하면 dp[i]가 결정되는 거야.
'''