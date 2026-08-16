# 문제 : 강수 확률 수치 얻고 그 수치에서 날씨를 문자열로 표시
# 접근 : 0이상 30이하 -> sunny, 31이상 70이하 -> cloudy, 71이상 -> rainy
n = int(input())

if 0 <= n <= 30:
    print("sunny")
elif 31 <= n <= 70:    
    print("cloudy")
else:
    print("rainy")