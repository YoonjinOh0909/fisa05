import hello

al = {a : a+1 for a in range(4) if a % 2 == 0}
type(al)
b = dict(
    first = list(al.keys()),
    second = list(al.values())
)
print(b)
type(b)