#★ 쇠막대기
import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
mak_lst = [i for i in input()]

stack = []
cnt = 0
for i in range(len(mak_lst)):
    if mak_lst[i] == '(':
        stack.append(mak_lst[i])
    else: ## ')'
        if mak_lst[i-1] == '(':
            stack.pop()
            cnt+= len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)

