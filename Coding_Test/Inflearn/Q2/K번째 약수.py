import sys
sys.stdin = open('input.txt','rt')
N, K = map(int,input().split())

st_num = 0
c_num = 0
for num in range(1,N+1):
    c_num +=1
    if N%num == 0:
        st_num +=1
    if st_num == K:
        print(num)
        break
    else:
        if c_num == N:
            print(-1)