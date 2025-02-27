import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1  

while B > A:
    if B % 2 == 0: 
        B //= 2
    elif B % 10 == 1: 
        B //= 10
    else:  
        print(-1)
        exit()
    cnt += 1 

print(cnt if A == B else -1) 