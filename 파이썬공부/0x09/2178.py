from collections import deque

n, m = [*map(int,input().split())] # n은 세로 길이(x), m 가로 길이 (y)
board = [] # 기본 정보가 들어올 board

for _ in range(n):
    board.append(list(map(int,list(input()))))

vis = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for x in range(n):
    for y in range(m):
        if vis[x][y] != 0 or board[x][y] != 1: # 만약 vis[x][y]에 다녀와서 0이 아니거나, board[x][y]가 1이 아니라서 길이 아니면 넘어간다.
            continue
        Q = deque()
        Q.append((x,y)) # 시작하는 곳이기 때문에 list에 넣어둔다.
        vis[x][y] = 1 # 시작하는 곳을 1로 둔다.
        while len(Q) != 0: # 만약 len(Q)가 0이면 비었다는 것이니 나간다.
            cur = Q.popleft()
            for i in range(4):
                nx = cur[0] + dx[i]
                ny = cur[1] + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m: # 만약 범위 밖이라면
                    continue
                if vis[nx][ny] != 0 or board[nx][ny] != 1 : # 만약 이미 들렸거나 길이 아니라면
                    continue
                vis[nx][ny] = vis[cur[0]][cur[1]] + 1 # 이전 칸의 값보다 +1 하면된다.
                Q.append((nx, ny))

print(vis[n-1][m-1])