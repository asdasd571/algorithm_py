import sys
input = sys.stdin.readline
N = int(input())
s = set()

for i in range(N):
    tmp = input().split()
    if len(tmp)==1:
        if tmp[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue
    command,target = tmp[0], int(tmp[1])

    if command == 'add':
        s.add(target)
    elif command == 'remove':
        s.discard(target)
    elif command == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)
    else:
        print(1 if target in s else 0)