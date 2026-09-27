# 문제 : 최고기온과 최저기온에 따라 하루 기온 변화 출력
# 접근 : 최고기온t - 최저기온u로 온도차 출력
t, u = map(int, input().split())
print(t - u)