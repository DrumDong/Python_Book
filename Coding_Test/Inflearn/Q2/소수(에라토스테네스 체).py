import sys
sys.stdin = open('input.txt','rt')
N = int(input())

# # 강사님 방법
ch = [0] * (N+1)
cnt = 0
for i in range(2,N+1):
    if ch[i] ==0:
        cnt +=1
        for num in range(i,N+1,i):
            ch[num]=1
print(cnt)