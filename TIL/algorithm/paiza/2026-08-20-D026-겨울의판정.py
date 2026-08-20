# 문제 : 최저 기온에 따라 겨울 판정
# 접근 : 최저기온 0도미만 -> W 출력, 그 외 최저 기온 출력
T = int(input())

if T < 0:
    print("W")
else:
    print(T)