def solution(info, n, m):
    # info = [[1, 2], [2, 3], [2, 1]]
    # n = 4
    # m = 4

    # dp 활용
    # dp[i][j] 
    # i 번째 물건까지 고려해서, a의 흔적이 j 일 때 b의 최소흔적을 표현.

    cnt = len(info) # 물건의 개수

    dp = [[float('inf')] * n for _ in range(cnt+1) ]
    dp[0][0] = 0

    for i in range(cnt): # 옷을 하나씩 고려
        for_a, for_b = info[i]
        for j in range(n) : # a는 0 ~ n-1까지만 가능

            if dp[i][j] == float('inf'): # 만약 아직 inf 값을 가지고 있는 다는 것은 해당 물건까지 고려했을 때, A가 i만큼 흔적을 남기지 않았다는 것
                continue

            # 만약 A가 훔친다면.
            # 최종 A =  현재 A 흔적 + 현재 물건의 흔적
            suma = j + for_a
            if suma < n: # 안 넘는 선이라면
                dp[i+1][suma] = min(dp[i+1][suma], dp[i][j]) # 물건 1개 고려했기 때문에 i + 1, b흔적에는 영향이 없기 때문에 현재 dp[i][j] 중 작은값으로
            
            # 만약 B가 훔친다면
            sumb = dp[i][j] + for_b
            if sumb < m:
                dp[i+1][j] = min(dp[i+1][j], sumb) # B가 훔쳐서 j는 변함이 없음. 하지막 비교하는 것은 원래 값 vs 새로운 b 흔적 값.

    min_a = float('inf')
    min_b = float('inf')

    print(dp)
    for a_n in range(n):
        if dp[cnt][a_n] != float('inf'):
            if dp[cnt][a_n] < m:
                return a_n
    return -1




solution([[1, 2], [2, 3], [2, 1]],	4,	4)
# 2