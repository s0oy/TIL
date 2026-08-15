# 문제 : 해수온도가 25도 이상이면 헤엄치려고함
# 접근 : 해수온도가 25 이상이면 "OK"출력, 25미만이면 "NG"출력
t = int(input())
if t >= 25:
    print("OK")
else:
    print("NG")