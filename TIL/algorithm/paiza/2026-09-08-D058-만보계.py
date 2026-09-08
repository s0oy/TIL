# 문제 : 기록한 일수와 걸음 수의 데이터를 사용해 하루 걸음 수 평균 구하기 
# 접근 : 걸음 수a를 n번 반복해 평균 구함
N = int(input())
a = [int(input()) for _ in range(N)]
print(sum(a) // N)