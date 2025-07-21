# 입력을 받을 때 남자,여자 구분과 학년을 받는다. 

# grade = [0] * 6
# gender_grade = [grade] * 2


# cnt = [*map(int, input().split())]
# maxV = cnt[1]
# for i in range(0, cnt[0]):
#     arr = [*map(int, input().split())]
#     print(f"arr {arr}")
#     gender_grade[arr[0]][arr[1]-1] += 1
#     print(gender_grade)
# ans = 0

# for i in gender_grade:
#     for j in i :
#         ans += (j+1)//2
# # print(gender_grade)

# print(ans)

# # arr = [[1,2], [3,4]]
# # print(arr[0][1])

student_cnt = [[0]*6, [0]*6]

total_cnt, maxV = [*map(int,input().split())]

for i in range(0, total_cnt):
    gender, grade = [*map(int, input().split())]
    student_cnt[gender][grade-1] += 1

ans = 0

for i in range(0,2):
    for j in range(0,6):
        ans += (student_cnt[i][j]+(maxV-1)) // maxV
print(ans)