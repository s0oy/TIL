# 문제 : 쾌적하게 보내기 위한 습도 측정
# 접근 : 적정 습도 60이하, 60이하 -> OK, 60이상 -> NG
h = int(input())
if h <= 60:
    print("OK")
else:
    print("NG")