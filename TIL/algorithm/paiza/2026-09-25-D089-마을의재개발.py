# 문제 : m개월 후 A마을 인구 출력
# 접근 : 기존 A마을에 100명 있음 -> 매달 n명씩 증가
#       기존 인원수 + 매달 n명 수 * m개월 후 인구
n = int(input())
m = int(input())
print(n * m + 100)