k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

day = len(score)
honor = []
result = []
for idx, s in enumerate(score):
    if idx < k:
        honor.append(s)
    else:
        # 새로 입력된 것이 honor의 최소보다 클 때
        if min(honor) < s:    
            # 작은 값 빼고 새로운 s 넣는다.
            honor.pop(honor.index(min(honor)))
            honor.append(s)

    result.append(min(honor))

result
