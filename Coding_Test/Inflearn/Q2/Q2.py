import sys
sys.stdin = open('input.txt','rt')
T = int(input())
for t in range(T):
    N,s,e,k = map(int,input().split(' '))
    a = list(map(int,input().split(' ')))

    a= a[s-1:e]
    a.sort()
    print('#%s'%(t+1),a[k-1])