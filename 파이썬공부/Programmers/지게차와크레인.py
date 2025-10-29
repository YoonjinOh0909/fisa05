# storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]	
# requests = ["A", "BB", "A"]	
# # 11

# storage = ["HAH", "HBH", "HHH", "HAH", "HBH"]
# requests = ["C", "B", "B", "B", "B", "H"]

# column = len(storage[0])
# row = len(storage)

# board = [ [True] * column for _ in range(row)] # 치우면 False로 바꿈

# dx_dy = [(1,0), (0, 1), (-1,0), (0, -1)] # 아래, 오른, 위, 왼
# from collections import deque
# # k = deque((1,2))
# # k = deque()
# # k.append((2,3))
# # k
# def canout(i, j):
#     d = deque([(i,j)])
#     move = [[False] * column for _ in range(row)]
#     move[i][j] = True

#     while(len(d) > 0):
#         nx, ny = d.popleft()
        
#         for dxdy in dx_dy:
#             dx,dy = dxdy
#             curx = nx + dx
#             cury = ny + dy
            
#             # 바깥쪽이랑 연결이 되어있다는 뜻
#             if curx < 0 or cury <0 or curx >= row or cury >= column:
#                 return True
#             if move[curx][cury] : # 이미 들린 곳이라면 넘어가면 된다.
#                 continue
#             if board[curx][cury] : # 부딪힌 곳이 True이면 아직 있다는 뜻
#                 continue
#             d.append((curx, cury))
#             move[curx][cury] = True

#     return False



# for re in requests:
#     if len(re) > 1: # 만약 2개 이상으로 나타나면 모든 알파벳 삭제한다.
#         for r in range(row):
#             for c in range(column):
#                 if storage[r][c] == re[0]:
#                     board[r][c] = False
#     else :
#         to_remove = list()
#         for r in range(row):
#             for c in range(column):
#                 # print(storage[r][c], re[0])
#                 # print(type(storage[r][c]), type(re[0]))
#                 if storage[r][c] == re[0] and canout(r,c):
#                     to_remove.append((r,c))
#         for rem in to_remove:
#             board[rem[0]][rem[1]] = False

# answer = 0
# for b in board:
#     answer += sum(b)

# print(answer)




# # node = deque()
# # for j in range(column):
# #     node.append((-1, j))
# #     node.append((row, j))

# # for i in range(row):
# #     node.append((i, -1))
# #     node.append((i, column))

# # for r in requests:
# #     new_deq = deque() # 아예 새로운 node
# #     backup_deq = deque() # 원래 node에서 다시 써야할 때

# #     while(len(node > 0)):
# #         n = node.popleft()
# #         nx, ny = n # 현재 node 좌표
# #         cnt = 0 # 만약 4가 되면 주변에 빈 것만 있다는 것으로 판단. 추후 계산할 필요 없음.
# #         for xy in dx_dy:
# #             dx, dy = xy  # 방향
# #             curx = nx + dx
# #             cury = ny + dy
# #             if curx < 0 or cury < 0 :
# #                 cnt += 1 # 범위에 벗어났다면 빈 곳이 있다는 것
# #                 continue


##############2025-10-29##############

storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests = ["A", "BB", "A"]
result = 11

n= len(storage) # 4
m = len(storage[0]) # 5

board = [[ 1 for _ in range(m)] for _ in range(n)]

dir = [(1,0), (0, 1), (0, -1), (-1, 0)]

from collections import deque

for req in requests:
    if len(req) > 1 : # 크레인으로 없애기
        for x, st_row in enumerate(storage):
            for y, val in enumerate(st_row):
                if val == req[0] :
                    board[x][y] = 0
        
    else : # 지게차로 없애기
        for_delete = list()
        for x, st_row in enumerate(storage):
            for y, val in enumerate(st_row):
                if board[x][y] == 0: # board가 0이면 이미 삭제가 된 상황.
                    continue
                if val != req[0] :
                    continue
                finish = False

                vis = [[ False for _ in range(m)] for _ in range(n)]

                dq = deque()
                dq.append((x,y))

                while(dq and not finish) : # dq 
                    qx, qy = dq.popleft()

                    for dx, dy in dir:
                        curx = qx + dx
                        cury = qy + dy

                        if curx < 0 or cury < 0 or curx >= n or cury >= m :
                            for_delete.append((x,y))
                            finish = True
                            break
                        if board[curx][cury] == 1:
                            continue
                        if vis[curx][cury] :
                            continue
                        dq.append((curx, cury))
                        vis[curx][cury] = True

        for del_x, del_y in for_delete:
            board[del_x][del_y] = 0

ans = 0
for b in board:
    ans = sum([ans, sum(b)])

print(ans)
