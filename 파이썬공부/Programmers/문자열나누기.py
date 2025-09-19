from collections import deque



a = "bananaa"

dq = deque(a)
cnt = 0
while(len(dq)!= 0):
    start_c = dq.popleft()
    sc = 1
    oc = 0
    while len(dq) != 0 and sc != oc: # 남은 것이 없거나, 시작한 char 개수와 other char의 개수가 다를 때
        next_c = dq.popleft()
        if start_c == next_c:
            sc = sc + 1
        else :
            oc = oc + 1
    
    cnt = cnt +1

print(cnt)