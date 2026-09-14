# 문제 : 7개 과목 평균점에 따른 합격 여부 판결
# 접근 : 합격 -> pass, 불합격 -> failure
scores = list(map(int, input().split()))

x = int(input())

total = sum(scores)
avg = total / 7

if avg >= x:
    print("pass")
else:
    print("failure")