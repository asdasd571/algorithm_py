import sys

input = sys.stdin.readline

# 유니온 파인드 함수 정의
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x != root_y:
        parent[root_y] = root_x  # 같은 집합으로 합침

# 입력 받기
N, M = map(int, input().split())

# 유니온 파인드 부모 테이블 초기화
parent = list(range(N + 1))

# 진실을 아는 사람 입력
know_info = list(map(int, input().split()))
know_number = know_info[0]
know = set(know_info[1:])  # 진실을 아는 사람 집합

# 파티 정보 저장
parties = []
for _ in range(M):
    party_info = list(map(int, input().split()))
    party_size = party_info[0]
    party_people = party_info[1:]
    parties.append(party_people)

    # 파티에 있는 사람들을 같은 그룹으로 묶기
    for i in range(1, party_size):
        union(party_people[i - 1], party_people[i])

# 모든 노드에 대해 find()를 수행하여 그룹을 압축
for i in range(1, N + 1):
    find(i)

# 진실을 아는 사람들의 최종 그룹 찾기
true_groups = set()
for person in know:
    true_groups.add(find(person))  # 진실을 아는 사람의 대표 노드 저장

# 과장할 수 있는 파티 개수 계산
count = 0
for party in parties:
    # 해당 파티에 진실을 아는 사람이 없는 경우 카운트 증가
    if all(find(person) not in true_groups for person in party):
        count += 1

# 결과 출력
print(count)
