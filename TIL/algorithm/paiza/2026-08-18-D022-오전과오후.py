# 문제 : 오전과 오후 표시하는 프로그램 만들기
# 접근 : 현재 시간 h, 0이상 12미만 -> AM, 12이상 24미만 -> PM
h = int(input())
if 0 <= h < 12:
    print("AM")
elif 12 <= h < 24:
    print("PM")