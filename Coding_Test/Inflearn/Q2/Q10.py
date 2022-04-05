import sys
#sys.stdin = open('input.txt','rt')

N = map(int,input().split())
Check_List = list(map(int,input().split()))

total_point = 0
bonus_point =0
for ck in Check_List:
    if ck != 0:
        total_point += 1
        total_point += bonus_point
        bonus_point +=1
    elif ck == 0:
        bonus_point = 0

print(total_point)