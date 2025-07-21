# 애너그램 만들기
# 순서를 바꿔서 같은 단어를 만들 수 있을 때의 관계를 애너그램이라고 함.
# 어떠한 단어 2개가 있을 때 최소 개수 제거하는 경우

# a = input()
# b= input()
# a_l = len(a)
# b_l = len(b)

# if a_l < b_l :
#     a,b = b,a

# count = 0
# for a_i in a:
#     if a_i in b:
#         count += 1
#         b = b.replace(a_i, "")
# print(a_l + b_l - count *2)



# li = [0] * 26

# a = input()
# b = input()

# for a_i in a:
#     li[ord(a_i)-97] += 1

# for b_i in b:
#     li[ord(b_i)-97] -= 1

# ans = 0

# for a in li:
#     if a > 0 :
#         ans += a
#     if a < 0:
#         ans -= a

# print(ans)

# a = 'aaabbaaccddee'

# print(a.replace('a','',4))

from collections import Counter

a = "ababcd"
b = "dfcb"
a_c = Counter(a)
print(type(a_c)) # collections.Counter
b_c = Counter(b)

print(sum((a_c - b_c).values()))
print(a_c)