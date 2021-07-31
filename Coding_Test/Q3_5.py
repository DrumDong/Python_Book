"""수들의 합 - 시간 초과"""
import sys
sys.stdin = open('input.txt','rt')

N,M = input().split()
num_list = list(map(int,input().split()))

init_count = 0
for idx,num in enumerate(num_list):
    init_list = []
    init_list.append(num)

    # 숫자 하나로 M을 만족할 경우 찾기
    if sum(init_list) == int(M):
        init_count+=1

    # 숫자 두개 이상으로 M을 만족할 경우 찾기
    elif sum(init_list) < int(M):
        for other_num in num_list[idx+1:]:
            init_list.append(other_num)
            if sum(init_list) > int(M):
                break
            elif sum(init_list) == int(M):
                init_count += 1
                break
    else:
        pass

print(init_count)

'''참조 노트 노션'''