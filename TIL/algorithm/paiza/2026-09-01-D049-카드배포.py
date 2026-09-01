# 문제 : 카드 배분 후 남는 카드의 매수 출력
# 접근 : 카드 매수n, 참가 인원수m, 1명에게 나누는 카드 매수p
#       인원수 * 1명이 받는 카드 매수 = 나눠준 총 카드 수
n = int(input())
m = int(input())
p = int(input())
print(n - (m * p))