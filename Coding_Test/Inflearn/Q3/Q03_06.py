#격자판 최대합

import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

N=int(input())
num_arr=[list(map(int,input().split())) for _ in range(N)]


init_row_sum = init_col_sum = 0
diag1_list =[]
diag2_list =[]
for idx in range(N):
    #row
    row=num_arr[idx]
    row_sum = sum(row)
    if row_sum > init_row_sum:
        init_row_sum = row_sum

    #col
    col_sum = 0
    for cdx in range(N):
        col_sum+=num_arr[cdx][idx]
    if col_sum > init_col_sum:
        init_col_sum = col_sum

    #diag
    diag1_list.append(num_arr[idx][idx])
    diag2_list.append(num_arr[N-idx-1][N-idx-1])

diag1_sum = sum(diag1_list)
diag2_sum = sum(diag2_list)

print(max([init_row_sum,init_col_sum,diag1_sum,diag2_sum]))