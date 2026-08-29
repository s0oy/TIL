# 문제 : 소지금 N으로 A 구입 여부 결과 출력
# 접근 : N이 A 금액 이상 -> Yes, 구입 못하면 -> No
A = 1000
N = int(input())
if N >= A:
    print("Yes")
else:
    print("No")