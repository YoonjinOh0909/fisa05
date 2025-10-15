dartResult = "1D2S#10S"

# 알파벳이 나오면 일단 점수 list에 추가한다. (그 조건에 맞게)
# *이나 #이 나오면 조건에 맞게 점수 list에서 처리한다.

grade_list = list()
cur_grade = 0
area = {"S" : 1, "D" : 2, "T" : 3}
for d in dartResult:

    if d.isnumeric() :
        cur_grade = 10 * cur_grade + int(d)
    elif d.isalpha() :
        grade_list.append(cur_grade ** area[d])
        cur_grade = 0
    else:
        if d == "#" : # 아차상으로 현재 점수를 * -1 한다.
            grade_list[-1] = grade_list[-1] * -1
        else :
            grade_list[-1] = grade_list[-1] * 2
            if len(grade_list) > 1 :
                grade_list[-2] = grade_list[-2] * 2
print(grade_list)
print(sum(grade_list))

######
# grade_list[-1] = grade_list[-1] * 2
# if len(grade_list) > 1 :
#     grade_list[-2] = grade_list[-2] * 2

# 위 코드를 
# grade_list[-2:] = [x * 2 for x in grade_list[-2:]]
# 로 표현할 수 있음.

