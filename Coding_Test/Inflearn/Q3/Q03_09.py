# 봉우리
import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
N = int(input())
B_arr = [list(map(int,input().split())) for _ in range(N)]

# 0 Padding 시키기
padding_B = []
for idx in range(N+2):
    if idx == 0 or idx == N+1:
        padding_B.append([0 for _ in range(N+2)])
    else:
        li = B_arr[idx - 1]
        li.insert(0,0)
        li.insert(N+1,0)
        padding_B.append(B_arr[idx-1])

# 봉우리 개수 찾기
CNT = 0
for r in range(1,N+1):
    for c in range(1, N + 1):
        if padding_B[r][c] > padding_B[r][c-1] and padding_B[r][c] > padding_B[r][c+1] and\
           padding_B[r][c] > padding_B[r-1][c] and padding_B[r][c] > padding_B[r+1][c]:
           CNT += 1

print(CNT)