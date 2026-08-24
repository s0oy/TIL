# 문제 : 3식량의 칼로리 합계에 따른 결과 출력
# 접근 : 목표치 이하 -> "OK", 목표치 이상 -> "NG"
x = int(input())
y_1,y_2,y_3 = input().split()

n = int(y_1) + int(y_2) + int(y_3)

if n <= x:
    print("OK")
else:
    print("NG")