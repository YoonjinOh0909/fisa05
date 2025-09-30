# 사과는 상태에 따라  1 ~ k 점수
# 한 상자에 사과 m개씩 포장
# 최저 점수 p, 가격 p * m
# 최대 점수를 가져가려면 최대한 최저 점수가 작은 것들이 몰려있어야 한다.
# 그러니 정렬해서 맨 뒤부터 가져가면 되지 않나

score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	
score_sort = sorted(score)
print(score_sort)
k = 4
m = 3
answer = 0
# while len(score_sort) >= m : # 만약 더 작다면 그냥 버린다.
#     cur_box = score_sort[m * -1:]
#     score_sort = score_sort[:m * -1]
#     answer = answer + min(cur_box) * m
#     print(f"score_sort {score_sort}")

# print(answer)
# 또 위 코드는 시간 초과가 뜬다.
# 아마 배열 복사가 계속 진행되니 그런 것이지 않을까

for i in range(len(score)-m, -1, -1 * m):
    print(f"i : {i} score_sort {score_sort[i]}")
    answer = answer +score_sort[i] * m

print(answer)


# 이게 최적의 답인듯.
#sorted(score)로 nlogn
#len(score)%m 을 하면 남겨지는 과일을 제하고 한 세트의 시작
    # 그리고 m만큼씩해서 값을 list한다
    # 어차피 m개씩 들어있으니 모두 sum해서 m을 곱한다.
sum(sorted(score)[len(score)%m::m])*m
sorted(score)[len(score)%m::m]