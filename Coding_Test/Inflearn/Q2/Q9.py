import sys
#sys.stdin = open('input.txt','rt')

N = int(input())

money_list = []
for idx in range(N):
    num_list = list(map(int, input().split())) # idx가 바뀔 때마다 새로운 Row 반환
    money = 0

    if len(list(set(num_list))) ==1:
        money = 10000 + num_list[0] * 1000
    elif len(list(set(num_list))) ==2:
        for num in num_list:
            if num_list.count(num) ==2:
                money = 1000 + num * 100
    else:
        money = max(num_list)* 100

    money_list.append(money)
print(max(money_list))