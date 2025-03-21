import sys
input = sys.stdin.readline()
N = int(input().split())


for i in range(N):
    tmp = input()
    if len(tmp)==1:
        if tmp[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue

    command, target = tmp[0],tmp[1]
    target = int(traget)

    if command == 'add':
        s.add(target)
    elif command == 'check':
        print(1 if target in s else 0)
    elif command == 'remove':
        s.discard(target)
    elif command == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)    
