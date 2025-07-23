# # L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# # D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# # B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# # 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# # P $	$라는 문자를 커서 왼쪽에 추가함

# init_str = list(input())

# cursor = len(init_str)
# ad_cnt = int(input())

# def moveLeft(cur : int):
#     if cur > 0 :
#         cur -= 1
#     return cur

# def moveRight(cur : int):
#     if cur < len(init_str):
#         cur += 1
#     return cur

# def deleteChar(cur : int):
#     if cur > 0:
#         init_str.pop(cur-1)
#         cur -= 1
#     return cur

# def insertChar(cur : int, input_char: str):
#     init_str.insert(cur, input_char)
#     cur += 1
#     return cur

# for i in range(ad_cnt):
#     i_s = list(input().split())
#     if i_s[0].lower() == 'l':
#         cursor = moveLeft(cursor)

#     elif i_s[0].lower() == 'd':
#         cursor = moveRight(cursor)

#     elif i_s[0].lower() == 'b':
#         cursor = deleteChar(cursor)

#     elif i_s[0].lower() == 'p':
#         cursor = insertChar(cursor,i_s[1])

# ans = ""

# for i in init_str:
#     ans += i

# print(ans)

# 위의 코드들은 시간 초과가 났음. 그 이유는 insert와 pop(n) 이 시간 복잡도 O(n)을 가지기 때문이다. 만약 1000개의 문자에서 1000번 진행하면 
# O(1000 * 1000) 이 되는 것이다.
# 따라서 다른 방식을 취해야 한다. insert 대신 append 를 사용, pop(n) 대신에 pop()을 사용한다.
# append는 list의 맨 뒤에 붙으며, pop()은 맨 뒤에 있는 요소를 제거한다.

import sys
input = sys.stdin.readline

left = list(input().strip())
right = []

cmd_cnt = int(input().strip())

for _ in range(cmd_cnt):
    cmd = list(input().strip().split())
    if cmd[0] == "L" and left:
        right.append(left.pop())
    elif cmd[0] == "D" and right:
        left.append(right.pop())
    elif cmd[0] == "B" and left:
        left.pop()
    elif cmd[0] == "P":
        left.append(cmd[1])

print("".join(left + right[::-1]))