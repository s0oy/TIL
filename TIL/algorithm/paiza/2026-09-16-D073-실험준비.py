# 문제 : 남은 약품의 양 출력
# 접근 : 총량 n밀리리터 약품을 a밀리리터씩 분리
#       -> n % a
n = int(input())
a = int(input())
print(n % a)