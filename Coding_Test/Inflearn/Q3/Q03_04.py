#두 리스트 합치기

import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
N= int(input())
N_list = list(map(int,input().split()))
M= int(input())
M_list = list(map(int,input().split()))
N_list.extend(M_list)
print(' '.join(str(num) for num in sorted(N_list)))