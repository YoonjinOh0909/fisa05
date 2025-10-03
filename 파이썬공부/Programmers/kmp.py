# Knuth-Morris-Pratt

arr = 'abacaaba'
arr = 'aaba'
def lps_def(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1,len(pattern)):
        while (j > 0) and (pattern[j] != pattern[i]):
            j = lps[j-1]

        if pattern[j] == pattern[i]:
            j = j+1
            lps[i] = j
           
    return lps
    
lps_def(arr)

def kmp(parents, pattern):
    results= list()
    j = 0
    lps = lps_def(pattern)
    for i in range(len(parents)):
        #만약 같지 않다면 돌아간다.
        while j > 0 and parents[i] != pattern[j]:
            j = lps[j-1]
        if parents[i] == pattern[j]:
            j = j + 1
            if j == len(pattern):
                results.append(i-j+1)
                j = lps[j-1]
    return results


# 예시 실행
text = "aabaacaadaabaaba"
pattern = "aaba"
print(kmp(text, pattern))  # 결과: [0, 9, 12]