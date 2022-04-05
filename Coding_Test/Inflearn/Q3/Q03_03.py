#카드 역배치

import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
N = 10
num_list = [i for i in range(1,21)]

for n in range(N):
    place_list= list(map(int,input().split()))
    rt_s = place_list[1]-1
    rt_f = place_list[0]-1

    change_list =[]
    for idx in range(rt_s,rt_f,-1):
        change_list.append(num_list[idx])
    change_list.append(num_list[rt_f]) # rt_f가 인덱싱이 안되기 때문에 반복문 이후에 추가

    for c_dx,idx in enumerate(range(rt_f,rt_s+1)):
        num_list[idx] = change_list[c_dx]

print(' '.join(str(i) for i in num_list))
