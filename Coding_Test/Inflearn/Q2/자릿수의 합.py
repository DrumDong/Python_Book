import sys
#sys.stdin = open('input.txt','rt')
N = int(input())
a = list(map(int,input().split()))

def digit_sum(x):
    x = str(x)
    SUM = 0
    for num in x:
        SUM += int(num)
    return SUM

sum_list =[]
for num in a:
    SUM = digit_sum(num)
    sum_list.append(SUM)

c_num = 0
for num in sum_list:
    if num > c_num:
        c_num = num

max_idx=sum_list.index(c_num)
print(a[max_idx])