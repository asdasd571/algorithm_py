import sys
input = sys.stdin.readline
N, M = map(int, input().split())

no_listen = []
no_see = []

for i in range(N):
    target_listen = input().strip()  # 입력값 끝의 공백을 제거하기 위해 .strip() 사용
    no_listen.append(target_listen)

for i in range(M):
    target_see = input().strip()  # 동일하게 .strip() 사용
    no_see.append(target_see)

# 두 리스트의 교집합 구하기
s = set(no_listen) & set(no_see)

# 정렬된 결과 출력
s = sorted(s)

print(len(s))
for person in s:
    print(person)
