# 문제 : 필요한 분의 물을 준비할 수 있는 경우에 따른 결과 출력
# 접근 : 준비할 수 있음 -> "Yes", 없다면 -> "No"
N = int(input())
a = int(input())

if a <= N:
    print("Yes")
else:
    print("No")