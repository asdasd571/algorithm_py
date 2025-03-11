# import sys
# input = sys.stdin.readline

# N = int(input())
# cnt = 0

# def hanoi(n,a,b,c):
#     global cnt
#     if(n==1):
#         print(a,c)
#         cnt+=1
#         return
    
#     else:
#         hanoi(n-1,a,c,b)
#         print(a,c)
#         cnt+=1
#         hanoi(n-1,b,a,c)

# print(2**N-1)
# hanoi(N,1,2,3)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)  # 바로 출력
        return
    hanoi(n-1, a, c, b)
    print(a, c)  # 바로 출력
    hanoi(n-1, b, a, c)

print(2**N - 1)  # 총 이동 횟수 출력
if N<=20:
    hanoi(N, 1, 2, 3)
  
