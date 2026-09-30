# 문제 : 7일간의 강수 확률에 따른 나가는 일수의 합계 출력
# 접근 : sum(int(input()) <= 30 -> 입력받은 강수 확률이 30이하 True
#                                 초과이면 False로 처리
#       sum(...) -> 7번 동안 참이 나온 횟수 모두 더해 출력
print(sum(int(input()) <= 30 for _ in range(7)))