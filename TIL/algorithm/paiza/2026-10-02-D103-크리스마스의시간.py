# 문제 : 25일의 현재 시각에 따른 크리스마스 판정
# 접근 : s * 60 + t -> 일몰 시각을 분 단위 정수로 변환
#       h * 60 + m -> 현재 시각을 분 단위 정수로 변환
# 막힌점 : print(...)부분 삼항 연산자 표현식 사용
#         <= 를 사용해 현재 시각이 일몰 시각과 같거나 
#         그 이전인가를 기준으로 참 거짓 값 출력
s, t = map(int, input().split())
h, m = map(int, input().split())

sunset = s * 60 + t
current = h * 60 + m

print("Yes" if current <= sunset else "No")