# 문제 : 특정 숫자를 받고 오류 유형 분류하기
# 접근 : 백의 자리가 2 -> ok, 백의 자리가 4 -> error, 그 외 -> unknown
n = input()
if n[0] == "2":
    print("ok")
elif n[0] == "4":
    print("error")
else:
    print("unknown")