# 스도쿠 검사
import sys
sys.stdin = open('C:/Users/Owner/Desktop/Coding Test/input.txt','rt')
sdoku = [list(map(int,input().split())) for _ in range(9)]
check = 'someting'

for rdx in range(9):
    # row check
    if len(set(sdoku[rdx])) == 9:
        pass
    else:
        check = 'NO'
        print('NO')
        break

    # 3*3 check -> 행고정, 열변환
    if rdx == 0 or rdx == 3 or rdx == 6:
        check_list0 = []
        check_list1 = []
        check_list2 = []
    else:
        pass

    check_list0.extend(sdoku[rdx][0:3])
    check_list1.extend(sdoku[rdx][3:6])
    check_list2.extend(sdoku[rdx][6:9])


if check != 'NO':
    if len(set(check_list0)) == 9 and len(set(check_list1)) == 9 and len(set(check_list2)) == 9:
        print('YES')
    else:
        print('NO')