# 문제 : 규칙에 따라 암호 해독
# 접근 : 1 -> A, 2 -> B, 0 -> C 
# 막힌점 : result="" -> 빈 문자열 초기화
S = input()

result = ""

for char in S:
    if char == "1":
        result += "A"
    elif char == "2":
        result += "B"
    else:
        result += "C"
        
print(result)