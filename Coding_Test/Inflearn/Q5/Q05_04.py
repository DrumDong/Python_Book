#후위식 연산
import sys
#sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
num_arr =input()

stack = []
for i in num_arr:
    try:
        stack.append(int(i))
    except:
        bi = stack.pop()
        fi = stack.pop()

        if i == '*':
            stack.append(fi*bi)
        elif i == '/':
            stack.append(fi / bi)
        elif i == '+':
            stack.append(fi + bi)
        elif i == '-':
            stack.append(fi - bi)

