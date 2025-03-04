from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().strip().split())

visited = [0] * 200001  # 시간 갱신


def bfs():
    ans_sec = 100001  # 최종 빠른 시간 저장하는 변수

    q = deque()
    ans_cnt = 0  # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수
    q.append(n)
    visited[n] = 0

    while q:
        x = q.popleft()
        if visited[x] > ans_sec:
            break
        if x == k:
            if ans_sec == 100001:
                ans_sec = visited[x]

            if visited[x] == ans_sec:
                ans_cnt += 1
            continue
        arr = [x - 1, x + 1, x * 2]

        for a in arr:
            if 0 <= a <= 200000 and (visited[a] == 0 or visited[a] == visited[x] + 1):
                visited[a] = visited[x] + 1
                q.append(a)
    return ans_sec, ans_cnt


ans_sec, ans_cnt = bfs()

print(ans_sec)
print(ans_cnt)