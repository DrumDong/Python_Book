import sys
sys.stdin = open('input.txt','rt')
N = int(input())

res = 0
fr = bc = N//2
for num in range(N):
    tree_list = list(map(int,input().split()))
    if num < N//2:
        for choice_num in range(fr,bc+1):
            res+= tree_list[choice_num]
        fr -= 1
        bc += 1
    else:
        for choice_num in range(fr,bc+1):
            res+= tree_list[choice_num]
        fr += 1
        bc -= 1

print(res)      
