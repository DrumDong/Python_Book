import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
num_arr =input()

print(num_arr)
print_list =[]
stack = []

for i in num_arr:
    try:
        int(i)
        print_list.append(i)
    except:
        if stack == []: # 비어있으면,
            stack.append(i)
        else:
            if i != '(':
                if (stack[-1] == '*' or stack[-1] == '/') and (i =='*' or i =='/'):
                    op = stack.pop()
                    print_list.append(op)
                elif (stack[-1] == '+' or stack[-1] == '-') and (i =='+' or i =='-'):
                    op = stack.pop()
                    print_list.append(op)
            elif stack[-1] == '(':
                if (stack[-1] == '*' or stack[-1] == '/') and (i =='*' or i =='/'):
                    op = stack.pop()
                    print_list.append(op)
                elif (stack[-1] == '+' or stack[-1] == '-') and (i =='+' or i =='-'):
                    op = stack.pop()
                    print_list.append(op)

    print(stack)
print(print_list)