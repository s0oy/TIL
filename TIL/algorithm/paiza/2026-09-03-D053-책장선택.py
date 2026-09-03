# 문제 : 2개의 숫자를 입력받아 두 숫자의 합에 따른 결과 출력
# 접근 : 합계가 16미만 -> "HIT", 16이상 -> "STAND"
n,m = map(int, input().split())
if n + m < 16:
    print("HIT")
else:
    print("STAND")