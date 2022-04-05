import sys
#sys.stdin = open('input.txt','rt')
N,K = map(int,input().split())
num_list = list(map(int,input().split()))

sum_list = []
for i in range(N):
    for j in range(i+1,N):
        for z in range(j + 1, N):
            sum_list.append(num_list[i]+num_list[j]+num_list[z])

sum_list=list(set(sum_list))
sum_list.sort()
print(sum_list[-3])
