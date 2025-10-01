# 1 대 1로 대결, 음식의 종류와 양이 바뀜.
# 한 선수는 제일 왼쪽부터, 한 선수는 오른쪽부터
# 중앙에 물이 있음.

# food = [1, 3, 4, 6]
food = [1, 7, 1, 2]

order = list()
for idx, val in enumerate(food[1:]):
    print(idx , val, val//2)
    order.append(str(idx+1) * (val//2))
''.join(order)+'0'+''.join(reversed(order))


