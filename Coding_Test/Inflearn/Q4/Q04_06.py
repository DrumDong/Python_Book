# 씨름 선수(그리디)
import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

n = int(input())
info_list = [tuple(map(int,input().split())) for _ in range(n)]

#print(info_list)
info_list.sort(reverse=True)

init_num = 0
c_num = 0
for num in range(n):
    w = info_list[num][1]
    if w > init_num:
        init_num = w
        c_num +=1

print(c_num)