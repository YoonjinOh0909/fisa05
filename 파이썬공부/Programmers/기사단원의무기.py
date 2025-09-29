# 기사단에게는 1 ~ number 지정.
# 약수의 개수 해당하는 공격력.
# 여기서 key point는 약수의 개수를 구하는 문제.
    # 약수의 개수를 구할 때는 1 ~ n * 1/2 까지 n으로 나눴을 때 나머지가 0 이 되는 숫자들의 합
    # 이렇게 해서 나온 숫자들의 개수 * 2를 한게 약수의 개수이다.
        # 하지만 여기서 제곱근이 정수일 때를 조심해야한다. 
        # 16을 예시를 들어보자
        # 1,2,4,8,16이 약수라 개수는 5개이다.
        # 하지만 n ** 1/2는 4이다. 16을 1 ~ 4까지의 정수 중 나눴을 때 0이 되는 것은 1,2,4로 3개있다.
        # 단순히 * 2를 해버리면 개수가 6이 되어 틀린 값이된다.
        # 그렇기 때문에 만약 나머지가 0이면 set()에 추가하여 중복 값을 없앤다.
number = 10 
# 1 2 3 4 5 6 7 8 9 10
# 1 2 2 3 2 4 2 4 3 4
# 1 2 2 3 2 2 2 2 3 2
limit = 3
power = 2

pow_list = list()

for n in range(1, number+1): # 각 기사단 하나씩.
    num = set()
    for i in range(1, int(number ** 1/2)+1):
        if n % i == 0:
            num.add(int(i))
            num.add(int(n/i))
    pow_list.append(len(num)) # 약수의 개수만큼 pow_list에 들어가도록 한다.

final_list = [p if p <= limit else power for p in pow_list]
# print(final_list)
print(sum(final_list))
# print(list(num))
# print(len(num))

# 사고자 하는 무기의 공격력이 제한수치보다 크다면, 미리 정한 수치의 무기 구매.


# 하지만 여기서 한 가지 간과한 점이 있다. 
# 만약 한 숫자의 약수만 구한다면, 위 방식으로 하는게 맞지만 1 ~ n의 약수를 구한다면 옳지 못하다.
#  n * sqrt(n) 의 시간 복잡도를 가지게된다. 물론 n ^ 2 보다는 작지만 그래도 크다.
# 100 sqrt -> 10 lon -> 2
# 그렇다면 어떻게 작성하는 것이 가장 적게 들까? -> 체를 이용하는 것이다.

# 1 ~ n 까지의 약수를 구하는 방법
number = 10 
limit = 3
power = 2

all_divisions = [[] for _ in range(number)] # 각 개수만큼으로 약수를 넣을 수 있는 list를 만든다.

for i in range(1, number+1): # 1 ~ number까지
    for j in range(i, number+1, i): # i부터 i씩 커지는 애들은 i를 약수로 가질 것이다.
        all_divisions[j-1].append(i)

# n = 1 일 때 N / 1
# n = 2 일 때 N -1 / 2
# n = 3 일 때 N -2 / 3
# n = n 일 때 N - (N-1) / n

# 따라서 N * (1 + 1/2 + 1/3 + ... + 1/n)이 된다.
# 뒤 수식은 조화 급수로 logN이 된다. 

sum_val = [len(i) for i in all_divisions]
after_limit = [j if j <= limit else power for j in sum_val]
print(sum(after_limit))

# 따라서 원래 2623.74ms 나오던게 14.60ms 나오는 것을 확인.