# a = int(input())
# b = int(input())
# c = int(input())

# val = str(a * b * c)

# ans = [0] * 10

# for v in val:
#     ans[int(v)] += 1

# for a in ans:
#     print(a)

mul = str(int(input()) * int(input()) * int(input()))
for i in range(10):
    print(mul.count(str(i)))