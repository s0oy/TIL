# 문제 : 받은 과자의 종류와 금액에 따른 반환 금액 출력
# 접근 : 초콜릿 받은 경우 -> 2배, 케이크 받은 경우 -> 5배
S = input()
N = int(input())

if S == "chocolate":
    print(N * 2)
else:
    print(N * 5)