# babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	
# baby = ["aya", "ye", "woo", "ma"]
# a = "aabcd"

# a.replace("aa","11")

# if baby in babbling[0]:
#     print(a)

# def lps(pattern):
    

babbling = ["aya", "yee", "u", "maa"]
babbling =["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
baby = ["aya", "ye", "woo", "ma"]


answer = 0
for a in babbling:
    keepgoing = True
    beforeVal = ""
    i = 0
    while keepgoing:
        if i == len(a):
            # print("2")
            answer += 1
            break
        if len(a) - i < 2 :
            # print(f"i {i} a[i:] {a[i:]}")
            break
        
        keepgoing = False
        for wordcnt in [2,3]:
            if a[i:i+wordcnt] in baby:
                if beforeVal == a[i:i+wordcnt]: # 직전 값과 지금 값이 같으면 답이 될 수 x
                    break
                else : # 직전 값과 다르다면:
                    keepgoing = True
                    beforeVal = a[i:i+wordcnt]
                i += wordcnt # 현재 index 최신화
                break

print(answer)


####
# 항상 다른 사람의 코드를 보면 경이롭다.
for b in babbling:
    # 두 단어가 연속으로 있으면 안되니, 만약 이렇게 되어 있으면 넘어간다.
    if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
        continue    

    # 각 list에 있는 것들을 " "로 바꾸는 이유 wyeoo에서 ye 없애면 woo가 되는데, 그러면 woo 발음할 수 있다고 판단 되기 때문
    # 이 때 not 인 이유 : if에 문자열 "" 를 하면 false 처리가 된다. 
        # 따라서 우리가 원하는 것은 깔끔하게 없어졌을 때 정답처리하는 것이기 때문에 not "" 을 해준다.
    if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
        count += 1