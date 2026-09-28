# 문제 : n명의 아이들의 나이에 따른 콩 수 준비
# 접근 : n번 동안 입력받은 나이들을 모두 더해 최종 합계 계산
n = int(input())
print(sum(int(input()) for _ in range(n)))