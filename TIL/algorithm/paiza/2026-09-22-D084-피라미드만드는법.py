# 문제 : N단의 피라미드 필요한 인원수 출력
# 접근 : 1부터 n까지 합 구하고 나눔
n = int(input())

result = n * (n + 1) // 2
print(result)