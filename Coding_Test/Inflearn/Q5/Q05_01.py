# 가장 큰 수
import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
num_list, del_num = list(input().split(' '))
num_list = [int(i) for i in num_list]
del_num = int(del_num)

7823
# 3 -> 0
# 7

stack_list = []
for n in num_list:
    if del_num == 0:
        stack_list.append(n)
    else:

        if stack_list == []:
            stack_list.append(n)
        else:
            for bn in stack_list[::-1]:
                if bn < n:
                    stack_list.pop()
                    del_num -=1

                    if del_num == 0:
                        break
                else:
                    pass
            stack_list.append(n)

if del_num == 0:
    print(''.join(str(i) for i in stack_list))
else:
    print(''.join(str(i) for i in stack_list[:-del_num]))

########################################################################################################################

num, m = map(int, input().split())
num = list(map(int,str(num)))
stack = []
for x in num:
    while stack and m >0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

