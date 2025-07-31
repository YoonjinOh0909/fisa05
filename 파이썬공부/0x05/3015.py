import sys
input = sys.stdin.readline
cnt = int(input().strip())

li = []
ans = 0
for _ in range(cnt):
    val = int(input().strip())
    
    # [-][x] 라 할 때 [-][0]에는 키 정보, [-][1]에는 개수가 들어간다.
    while li and li[-1][0] < val : 
        ans += li[-1][1]
        li.pop()
    else:
        if li and li[-1][0] == val : # 같은 키가 들어온다면
            ans += li[-1][1] # 같은 개수가 있는 만큼
            li[-1][1] += 1 
            if len(li) > 1 : # 만약 자기 말고 다른 키가 있다면 자기 보다 큰 한 명과 짝을 이룰 수 있다는 뜻
                ans += 1
        else : #not li or li[-1][0] < val 일 경우
            if li : # 만약 하나라도 있다면 1개의 짝이 생길 수 있음.
                ans += 1
            li.append([val, 1])
print(ans)



##############
# 반례 4 3 3 3 2 2
# 
# import sys
# input = sys.stdin.readline
# cnt = int(input().strip())

# li = []
# ans = 0
# for _ in range(cnt):
#     val = int(input().strip())

#     while li and li[-1] < val: # li에 값이 들어있고, 가장 밖의 값이 val 보다 작을 경우 pop() 한다.
#         li.pop()
#         ans += 1
#     else :
#         if li and li[-1] > val :
#             ans += 1
#         if li and li[-1] == val :
#             ans += len(li)
#         li.append(val)
    
# print(ans)

################
# 반례 : 4 3 2 1
# import sys
# input = sys.stdin.readline
# cnt = int(input().strip())

# li = []
# ans = 0
# for _ in range(cnt):
#     val = int(input().strip())

#     while li and li[-1] < val: # li에 값이 들어있고, 가장 밖의 값이 val 보다 작을 경우 pop() 한다.
#         li.pop()
#         ans += 1
#     else :
#         ans += len(li)
#         li.append(val)
    
# print(ans)

