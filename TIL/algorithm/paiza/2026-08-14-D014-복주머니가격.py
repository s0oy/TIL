# 문제 : n엔의 복주머니 안 두 상품의 정가 a엔, b엔 조사 후 정가보다 유익한지 출력
# 접근 : 전체 n엔에서 정가 a + b한 값을 뺌
n = int(input())
a = int(input())
b = int(input())
print((a + b) - n)