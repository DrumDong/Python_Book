import sys

#sys.stdin = open('input.txt','rt')
num_list = list(map(int,input().split()))
SongLen_list= list(map(int,input().split()))

lt =1
rt = sum(SongLen_list)
#print(lt,rt)

res = 0
while lt<=rt:
    mid = (lt+rt)//2

    elbum_list = []
    cnt = 1 # 노래가 들어가기 전에 이미 주머니가 생성되기 때문임
    for num in SongLen_list:
        elbum_list.append(num)

        if sum(elbum_list) > mid:
            elbum_list = [num]
            cnt += 1

    if cnt <= num_list[1]:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)