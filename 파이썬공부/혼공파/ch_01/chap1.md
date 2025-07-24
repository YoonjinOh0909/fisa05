### step_2_2.py 

#### 특수 변수
\_\_name\_\_ 은 파이썬에서 특수하게 정의된 변수.
본 파일에서 실행이 되면 \_\_name\_\_ 에는 \_\_main\_\_ 이 들어간다. 

하지만 다른 파일에서 import를 한 상태에서 실행이 되면 해당 모듈의 이름이 나온다. 
```py
# hello.py
print(__name__) #__main__
```

```py
#importhello.py
import hello 

# hello
```

#### 글로브 패턴
와일드카드 문자를 활용하여 특정 조건을 만족하는 파일의 집합을 표현 하는 것.

|와일드카드| 의미	|예시|
|---|---|---|
|*	|임의의 0개 이상의 문자|*.txt → 모든 txt 파일
|?	|임의의 1개 문자|a?.py → a1.py, ab.py 등
|[abc]|a, b, c 중 하나|file.txt → file1.txt, file2.txt
|[a-z]|	a~z 중 하나|	file[a-c].txt → filea.txt, fileb.txt, filec.txt

