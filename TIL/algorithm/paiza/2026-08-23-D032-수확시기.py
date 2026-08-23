# 문제 : 3가지 야채 중 처음 수확할 수 있는 것 며칠 후인지 출력
# 접근 : 작은 수를 구할 수 있는 min을 사용해 처음 수확하는것 출력
d_1 = int(input())
d_2 = int(input())
d_3 = int(input())
print(min(d_1, d_2, d_3))