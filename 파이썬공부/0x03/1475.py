# 1. 숫자가 주어지면 0~9번까지의 숫자들이 각각 몇 개 있는지 파악한다.
# 2. 6과 9는 1세트에서 최대 2개 사용 가능. 따라서 (6 개수 + 9개수 /2)로 한다.

# val = input()
# arr = [0] * 10
# for a in val:
#     arr[int(a)] = val.count(a)
# sixNnine = arr[6] + arr[9]
# arr[6] = 0
# arr[9] = int(sixNnine/2) + sixNnine%2

# print(*sorted(arr)[-1:])

val = input()
arr = [0] * 10
for a in val:
    arr[int(a)] = val.count(a)
arr[6] = arr[9] = (arr[6] + arr[9] + 1) // 2

print(max(arr))

