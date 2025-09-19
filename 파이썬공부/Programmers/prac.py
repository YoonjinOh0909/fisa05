a = "anc"
list(a)

a = 12

cnt  = 0
for i in range(1,a+1):
    if (a % i) == 0:
        cnt = cnt + 1

print(cnt)
# 1,2,3,4,6,12

# 1 2 4 8 16
# i * i = a 라면 지금까지 cnt + 1s
6 ** 0.5


cnt  = 0

a = 16
r = set()
for i in range(1,int(a**0.5)+1):
    if a % i == 0:
        r.add(i)
        r.add(a//i)

print(r)

help(r.discard)

len(r)

type(sorted(r))
type(r)

k = set()
k.add(1)
k.add(2)
k.update([2,3])
k

a = [1,2,3,4]

a = [1, 2, 3, 4]
result = [x if x > 1 else 0 for x in a ]
print(result)  # [2, 3, 4]