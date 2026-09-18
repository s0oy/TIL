# 문제 : 매번 n책 모두 교환할 경우 몇 번 교환 가능한지와 남은 갯수
# 접근 : 기기에 필요한 횟수n, 구입한 전지의 갯수m
#       m을 n으로 나눈 몫 -> m // n, 나머지 -> m % n
n = int(input())
m = int(input())

print(m // n)
print(m % n)