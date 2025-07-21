# s = input()
# alpha = "abcdefghijklmnopqrstuvwxyz"
# arr =[0 for _ in range(0, 26)]

# for ss in s:
#     arr[alpha.index(ss)] += 1

# for a in arr:
#     print(a, end =" ")

s = input()
arr = [0] * 26

for ss in s:
    arr[ord(ss)-97] += 1
print(*arr)