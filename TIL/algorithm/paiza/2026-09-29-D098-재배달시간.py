# 문제 : 당일중에 짐이 도착하는 경우에 따라 결과 출력
# 접근 : n시 이전에 재배달 의뢰 시 당일 짐 도착
#       m시에 재배달 의뢰했을 경우 당일중에 짐 도착 -> OK
#       그 외 -> NG
n = int(input())
m = int(input())

if n >= m:
    print("OK")
else:
    print("NG")