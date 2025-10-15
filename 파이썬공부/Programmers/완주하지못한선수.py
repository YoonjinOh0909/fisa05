participant = ["marina", "josipa", "nikola", "vinko", "filipa", "filipa", "filipa"]
completion = ["marina", "josipa", "nikola", "vinko", "filipa", "oh"]
ans = ""
# 먼저 set으로 계산을 해본다.
set_list = list(set(participant)-set(completion))
if len(set_list) > 0 :
    ans = set_list[0]

# 근데 만약 동명이인이 있다면
from collections import Counter
p = Counter(participant)
c = Counter(completion)

for name in p:
    if p[name] != c[name]: # 숫자가 다르다면
        ans = name
    
#######
# 위 코드 같은 경우 set의 시간복잡도가 더 효율적이라 판단해서 두 가지 상황으로 나눔.
# 하지만 set 생성 할 때도 O(n)이 걸리고 Counter로 생성할 때도 같다.
# 따라서 상관없이 Counter를 생성하면 된다. 여기에서 Counter도 차집합 연산을 할 수 있다.

# 게다가 Counter이기 때문에 value 값들은 int. 

# 그래서 key 값이 같은 상태에서 차집합을 하면 개수 차감이 된다.
