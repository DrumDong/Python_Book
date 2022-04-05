#공주 구하기(큐)
import sys
from collections import deque

sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
N, K = map(int,input().split()) # N: 왕자, K: 탈락 숫자

deq = deque([i+1 for i in range(N)])

i = 1
while len(deq) != 1:
    prince = deq.popleft()
    if i ==K:
        i=1
    else:
        deq.append(prince)
        i+=1



