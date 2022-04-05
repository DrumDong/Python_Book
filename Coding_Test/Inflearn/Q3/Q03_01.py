# 회문 문자열 검사

import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
N = int(input())
word_list = [input() for _ in range(N)]

for num,word in enumerate(word_list):
    lw = len(word)
    rv_list = []
    for idx in range(lw-1,0,-1):
        rv_list.append(word[idx])
    rv_list.append(word[idx-1])

    num +=1
    if word.lower() == ''.join(rv_list).lower():
        print('#%s %s'%(num,'YES'))
    else:
        print('#%s %s' %(num,'NO'))