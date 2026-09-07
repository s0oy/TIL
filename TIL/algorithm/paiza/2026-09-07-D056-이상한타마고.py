# 문제 : 3가지 계란을 각각 부화시키는데 필요한 최소 보행 거리 찾기
# 접근 : max를 사용해 최소 보행 거리 찾기
d_1, d_2, d_3 = map(int, input().split())
print(max(d_1, d_2, d_3))