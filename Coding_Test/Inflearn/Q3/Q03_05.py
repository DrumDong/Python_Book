#수들의 합 *_*

import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

N,M = map(int,input().split())
num_list = list(map(int,input().split()))

CNT_list = []
for idx,num in enumerate(num_list):
    sum_list =[num]

    if sum(sum_list)>M:
        pass
    elif sum(sum_list)==M:
        CNT_list.append(sum_list)
    else:
        for num2 in num_list[idx+1:]:
            sum_list.append(num2)
            if sum(sum_list) ==M:
                CNT_list.append(sum_list)
                break
            elif sum(sum_list) > M:
                break

print(len(CNT_list))