# 숫자만 추출

import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
word = input()

int_list =[]
for w in word:
    try:
        int(w)
        int_list.append(w)
    except:
        pass

num=int(''.join(int_list))
print(num)

CNT =0
for i in range(num+1):
    i = i+1
    if num%i ==0:
        CNT +=1

print(CNT)
