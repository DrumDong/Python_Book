import sys
#sys.stdin = open('input.txt','rt')

N = map(int,input().split())
num_list = list(map(int,input().split()))

def reverse(x):
    str_x  = str(x)
    len_x = len(str_x)

    new_x = ''
    for idx in range(len_x):
        idx = abs(idx-len_x+1)
        new_x += str_x[idx]
    new_x = int(new_x)

    return new_x

def IsPrime(x):

    check_list =[]
    for num in range(1,x+1):
        if x % num ==0:
            check_list.append(num)
    if len(check_list) ==2:
        print(x)

for num in num_list:
    reverse_num= reverse(num)
    IsPrime(reverse_num)


