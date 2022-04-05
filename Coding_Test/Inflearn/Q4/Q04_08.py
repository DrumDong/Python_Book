#침몰하는 타이타닉
import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')

N,M = map(int,input().split())
customer_list = list(map(int,input().split()))

cnt = 0
customer_list.sort()

while len(customer_list) != 0:

    if len(customer_list) ==1:
        cnt +=1
        break

    if customer_list[0] + customer_list[-1] > M:
        customer_list.pop()
        cnt += 1
    else:
        customer_list.pop(0)
        customer_list.pop()
        cnt += 1