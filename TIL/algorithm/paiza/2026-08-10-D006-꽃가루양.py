# 문제 : 평방 센티미터 당 꽆가루의 수 관찰
# 접근 : N > 100이면 "DANGER" 출력, 아니면 N 출력
N = int(input())
if N > 100:
    print("DANGER")
else:
    print(N)