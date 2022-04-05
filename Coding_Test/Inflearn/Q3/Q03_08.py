# 곳감(모래시계)
import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

N = int(input())
f_list = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
#rt_list = [list(map(int,input().split())) for _ in range(M)]

# 곶감판 회전
for _ in range(M):
    rt_list = list(map(int, input().split()))
    rt_num = rt_list[2]
    selected = f_list[rt_list[0]-1]

    # 회전수가 곶감 인덱스보다 큰 경우에는 슬라이싱이 제대로 적용되지 않음
    # 그렇기 때문에 전체 회전이 다돌고 남은 여분의 회전수만 남겨서 더해주어야함.
    if rt_num > N:
        rt_num = rt_num - N * (rt_num // N)

    new_list =[]
    if rt_list[1] == 0:
        new_list.extend(selected[rt_num:])
        new_list.extend(selected[:rt_num])
    else:
        new_list.extend(selected[N-rt_num:])
        new_list.extend(selected[:N-rt_num])

    # 회전된 곶감 리스트 반영
    f_list[rt_list[0] - 1] = new_list

# 합계 구하기 -> Q03_07 참고
total = 0
for n in range((N+1)//2):

    if n == (N//2):
        total += f_list[n][n]

    else:
        #위에서 아래로
        total += sum(f_list[n][0+n:N-n])

        #아래에서 위로
        total += sum(f_list[N-1-n][0+n:N-n])

print(total)