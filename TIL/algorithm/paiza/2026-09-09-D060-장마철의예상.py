# 문제 : 일기예보 데이터에 따른 장마철 여부 결정
# 접근 : 7일간 비오는 경우1, 맑은 경우0
#       비오는 날 5일이상 -> yes, 낮으면 -> no
# 막힌점 : weather.count("1") -> weather 리스트 안에 1이라는 값이 총 몇개인지 셈
weather = input().split()

if weather.count("1") >= 5:
    print("yes")
else:
    print("no")