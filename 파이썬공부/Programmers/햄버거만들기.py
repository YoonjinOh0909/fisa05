# 조리된 순서대로 아래서부터 위로 쌓이기.
# 빵 야채 고기 빵으로 쌓인 것만 포장.

# [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]
# [야채, 빵, 야채, 고기, 빵]

# 빵이 들어왔을 때 그걸 기준으로 [i -3 : i+1]를 확인?

# a = [1,2,3,4]
# del a[2:3]
# a

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
cur = list()
correct_set = [1,2,3,1]
answer = 0
for val in ingredient:
    cur.append(val)
    if len(cur) < 4: # 4보다 작으면 어차피 만들 수 없음
        continue
    if val == 1: # 빵이라면
        is_set = True
        for idx, cur_ing in enumerate(cur[-4:]):
            # print(idx, cur_ing)
            if cur_ing != correct_set[idx]:
                is_set = False
        if is_set == True:
            del cur[-4:]
            answer = answer + 1


print(answer)

# 코드를 보면 이와 같이 list를 비교할 수 있다.
# a = [0,1,2,3,4]

# if a[-4:] == [1,2,3,4]:
#     print("yes")

# 즉 위에 is_set 부분이 필요 없는 것이다.

# 뿐만 아니라 저렇게 했을 경우 뭐 len의 수가 몇일지 예상, 파악할 필요 없음 
# 따라서 len(cur) 부분을 삭제한다.

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
cur = list()
correct_set = [1,2,3,1]
answer = 0
for val in ingredient:
    cur.append(val)
    if val == 1: # 빵이라면
        print(cur[-4:])
        if cur[-4:] == correct_set:
            del cur[-4:]
            answer = answer + 1

print(answer)

# pop으로 4번을 할 수 있지만, 맨 뒤에 있는 것들을 삭제하는 것이기 때문에 del 사용한다.
# gpt 대답으로는 del이 근소하게 더 빠르다라는 답을 들었음.