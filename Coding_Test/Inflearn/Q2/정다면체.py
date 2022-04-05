import sys
sys.stdin = open('input.txt','rt')
N,M = map(int, input().split())

# 내 풀이
sum_list = []
for i in range(N):
    for j in range(M):
        sum_list.append(i+1+j+1)

sum_unique = list(set(sum_list))
sum_count = []
for sum in sum_unique:
    sum_count.append(sum_list.count(sum))

max_c = max(sum_count)

for idx,count in enumerate(sum_count):
    if count == max_c:
        print(sum_unique[idx],end=' ')

# 강사님 풀이
cnt = [0] * (n+m+3) # 3은 여유분으로 넣음.
max = -111111111111111 # 최소 카운트 초기값 지정
for i in range(1,N+1):
    for j in range(1, M+1):
        cnt[i+j]+=1
for i in range(n+m+1):
    if cnt[i]> max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i,end=' ')

#강사님 풀이
for i in range(N):
    for j in range(M):
        sum_list.append(i+1+j+1)

