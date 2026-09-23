# 문제 : 습도에 따라 결과 출력
# 접근 : 습도가 40이상 60이하 -> OK, 그 외 -> NG
n = int(input())

if 40 <= n <= 60:
    print("OK")
else:
    print("NG")