n = int(input())
arr = set([*map(int, input().split())])
x = int(input())

# 20250708 시간 초과
# cnt = 0
# for v in arr:
#     try :
#         ind = arr.index(x-v)
#     except:
#         pass
#     else :
#         if ind >= 0 :
#             cnt += 1
# print(cnt // 2)

# 250710 런타임 에러
# cnt = 0
# x_arr = [0] * (x+1)
# for av in arr :
#     x_arr[av] += 1

# for av in arr :
#     if x_arr[x-av] == 1 :
#         cnt += 1

# print(cnt // 2)

# 	메모리 : 46620 kb 시간 : 88 ms
# cnt = 0
# x_arr = [0] * (1000000)
# for av in arr :
#     x_arr[av] += 1

# for av in arr :
#     if x-av<1000000 and x -av > 0 and x_arr[x-av] == 1 :
#         cnt += 1

# print(cnt // 2)

cnt = 0
for i in arr:
    if x-i in arr:
        cnt+=1
print(cnt // 2)