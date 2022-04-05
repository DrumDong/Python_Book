# 격자판 회문수
import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

rt_list = [list(map(int,input().split())) for _ in range(7)]
num =0
for idx in range(7):
    r_list = []
    c_list = []
    for ddx in range(7):
        # 가로 검사
        r_list.append(rt_list[idx][ddx])
        if len(r_list) == 5:
            if r_list == list(reversed(r_list)):
                num+=1
            r_list.pop(0)

        # 세로 검사
        c_list.append(rt_list[ddx][idx])
        if len(c_list) == 5:
            if c_list == list(reversed(c_list)):
                num+=1
            c_list.pop(0)

print(num)