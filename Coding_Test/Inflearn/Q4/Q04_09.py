#증가수열 만들기(그리디)
import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

N = int(input())
num_list = list(map(int,input().split()))

lt = 0
rt = N - 1
last = 0
res = ""
tmp = []

while lt <= rt:
    if num_list[lt] < last and num_list[rt] < last:
        break

    if num_list[lt] > last:
        tmp.append(num_list[lt])
        res = res + 'L'
        lt +=1
    if num_list[rt] > last:
        tmp.append(num_list[rt])
        res = res + 'R'
        rt -=1
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        last =tmp[0]

    tmp = []

print(len(res))
print(res)
