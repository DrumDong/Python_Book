#창고 정리
import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
len_row = int(input())
box_list = list(map(int,input().split()))
M = int(input())

for _ in range(M):
    box_list.sort(reverse=True)
    print(box_list)
    max_value = box_list[0]
    min_value = box_list[-1]

    max_value = max_value - 1
    min_value = min_value + 1

    box_list[0] = max_value
    box_list[-1] = min_value

print('-----------')
print(box_list)
box_list.sort(reverse=True)
print(box_list[0] - box_list[-1])