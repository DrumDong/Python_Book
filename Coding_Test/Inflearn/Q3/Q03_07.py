# 사과나무(다이아몬드)
import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

N = int(input())
f_array=[list(map(int,input().split())) for _ in range(N)]

total = 0

for n in range((N+1)//2):
    print(n)
    if n == (N//2):
        total += sum(f_array[n])
        print('가운데',f_array[n])
    else:
        # 위에서 아래로
        total += sum(f_array[n][N//2-n:N//2+n+1])
        print('위',f_array[n][N//2-n:N//2+n+1])
        # 아래에서 위로
        total += sum(f_array[N-1-n][N//2-n:N//2+n+1])
        print('아래',f_array[N-1-n][N//2-n:N//2+n+1])

print(total)