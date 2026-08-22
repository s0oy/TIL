# 문제 : 문장에 따라 아이의 반응을 나타내는 문자열 출력
# 접근 : "candy" or "chocolat" -> "Thanks!", 그 외 -> "No!"
s = input()
if s == "candy" or s == "chocolate":
    print("Thanks!")
else:
    print("No!")