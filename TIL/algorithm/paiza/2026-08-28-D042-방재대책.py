# 문제 : 하루에 n개의 통조림 먹는 가정하 m일 분 구입 결정
#       1캔당 p엔으로 했을 때 합계 출력
# 접근 : 하루 소비량 n * 구입일수 m * 1캔당 가격p
n = int(input())
m = int(input())
p = int(input())
print(n * m * p)