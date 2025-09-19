```
코딩테스트 때 쓰면 좋은 코드
```

## deque
```python
from collections import deque
```

## str list 만들기
```py
a = "abc"
list(a) # ['a', 'b', 'c']
[a] # ['abc']
```

## append, extend
```py
a = ['a']
b= ['c','d']

a.append(b) # ['a', ['c','d']]

a = ['a']
b= ['c','d']

a.extend(b) # ['a', 'c', 'd']
```

## heapq
| 함수명         | 설명                             | 사용법 예시                          |
|--------------|--------------------------------|----------------------------------|
| heappush     | 힙에 원소 추가                   | `heapq.heappush(heap, item)`      |
| heappop      | 가장 작은 원소 삭제 및 반환       | `heapq.heappop(heap)`             |
| heapify      | 리스트를 힙으로 변환              | `heapq.heapify(list)`             |
| heapreplace  | 가장 작은 원소 제거 후 새 원소 추가 | `heapq.heapreplace(heap, item)`   |
| heappushpop  | 원소 추가 후 가장 작은 원소 제거 및 반환 | `heapq.heappushpop(heap, item)`   |
| nlargest     | 가장 큰 n개 원소 반환             | `heapq.nlargest(n, iterable)`     |
| nsmallest    | 가장 작은 n개 원소 반환           | `heapq.nsmallest(n, iterable)`    |

```python
import heapq

heap = []
heapq.heappush(heap, 4)                # heap: [4]
heapq.heappush(heap, 1)                # heap: [1, 4]
print(heapq.heappop(heap))             # 출력: 1, heap: [4]

lst = [3, 1, 7, 4]
heapq.heapify(lst)
print(lst)                            # 출력: [1, 3, 7, 4]

heapq.heapreplace(lst, 2)             # 1 제거 후 2 추가
print(lst)                            # 출력: [2, 3, 7, 4]

print(heapq.heappushpop(lst, 5))     # 2보다 5 추가 후 2 팝 → 출력 2
print(lst)                            # 출력: [3, 4, 7, 5]

print(heapq.nlargest(2, lst))        # 출력: [7, 5]
print(heapq.nsmallest(2, lst))       # 출력: [3, 4]

```

## 약수 구하기

```python
a = 16
s = set()
for i in range(1, int(a ** 0.5) + 1):
    if (a % i) == 0: # 만약 i로 나눴을 때 0이 된다면
        s.add(i)
        s.add(a // i)
# 나머지가 0일 때 i 를 s에 추가하고
# i로 나누는 몫을 s에 같이 추가한다.
# 이때 set으로 하기 때문에 중복된 값은 없다.
```

## set

| 메서드/함수           | 설명                                      | 예시                     |
|---------------------|-----------------------------------------|------------------------|
| add(x)              | 집합에 원소 x 추가                         | `s.add(4)`             |
| update(iterable)    | 여러 원소를 한꺼번에 추가                   | `s.update([5,6])`      |
| remove(x)           | 원소 x 제거 (없으면 KeyError 예외 발생)      | `s.remove(4)`          |
| discard(x)          | 원소 x 제거 (없어도 예외 없음)                | `s.discard(4)`         |
| pop()               | 임의 원소 제거 및 반환                       | `s.pop()`              |
| clear()             | 모든 원소 제거                             | `s.clear()`            |
| union(set2)         | 합집합 반환                               | `s.union(t)`           |
| intersection(set2)  | 교집합 반환                               | `s.intersection(t)`    |
| difference(set2)    | 차집합 반환                               | `s.difference(t)`      |
| symmetric_difference(set2) | 대칭 차집합 반환                     | `s.symmetric_difference(t)` |
| copy()              | set 복사                                 | `s.copy()`             |

|집합 연산자 | 기능        | 설명                     |
|--------|------------|------------------------|
| &#124; (or)  | 합집합       | 두 집합의 모든 원소 포함       |
| & (and) | 교집합       | 두 집합 모두에 있는 원소만 포함   |
| -      | 차집합       | 첫 집합에만 있는 원소 포함      |
| ^      | 대칭 차집합    | 두 집합 중 하나에만 있는 원소  |


## filter
```py
a = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, a))  # 짝수만 추출
print(result)  # [2, 4, 6]
```

## 리스트 컴프리헨션
```py
a = [1, 2, 3, 4]
result = [x for x in a if x > 1]
print(result)  # [2, 3, 4]
```