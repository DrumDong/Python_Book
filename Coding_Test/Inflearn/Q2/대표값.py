import sys
sys.stdin = open('input.txt','rt')
N  = int(input())
score_list  = list(map(int,input().split()))

# 내 풀이
avg = round(sum(score_list)/N,0)
min_cha = 100000000
for idx, score in enumerate(score_list):
    cha = abs(score-avg)
    st_num = idx+1
    st_score = score_list[idx]
    if cha < min_cha:
        min_cha  = cha
        min_st_num = st_num
        min_score = st_score
    elif cha == min_cha:
        if st_score > min_score:
            min_st_num = st_num
            min_score = st_score


print(int(avg),min_st_num)

#강사님 풀이


