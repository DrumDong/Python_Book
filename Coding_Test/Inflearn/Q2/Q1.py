import sys
#sys.stdin = open('input.txt','rt')
n, k = map(int,input().split()) # n 숫자, k 작은수의 번째
#print(n,k)


# 동규 문제 풀이
num_list =[]
for num in range(1,n+1):
    if n%num ==0:
        num_list.append(num)

if  len(num_list)<k:
    print(-1)
else:
    print(num_list[k-1])

# 강사 문제 풀이
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
