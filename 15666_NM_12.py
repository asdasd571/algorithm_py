import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))  # 중복 제거 후 정렬
ans = []

def dfs(start):  # start 변수를 추가하여 다음 선택할 숫자의 시작점 지정
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(start, len(arr)):  # start부터 시작하여 비내림차순 유지
        ans.append(arr[i])
        dfs(i)  # 다음 호출에서도 같은 숫자 또는 그 이후 숫자만 선택하도록 i를 전달
        ans.pop()

dfs(0)  # 시작 인덱스 0으로 초기 호출
