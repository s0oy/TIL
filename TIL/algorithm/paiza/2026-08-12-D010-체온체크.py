# 문제 : 체온 측정 후 출사 여부 결정 -> 37.0 이상이면 NG, 37.0 미만이면 OK
# 접근 : 체온을 입력받아 37.0과 비교하여 결과 출력
n = float(input())
if n >= 37.0:
    print("NG")
else:
    print("OK")