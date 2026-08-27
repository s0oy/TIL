# 문제 : 문자열에 기록된 맑은 날과 비의 날을 공백으로 구분해 출력
# 접근 : 맑은 날 -> S, 비오는 날 -> R
# 막힌점 : 공백을 .strip()하는 부분, 
#         문자열에 기록된 날을 셀 때 .count()를 사용하는 부분
n = int(input())
s = input().strip()
print(s.count('S'), s.count('R'))