# 문제 : 무작위로 선택한 10장의 잎 가운데 8장 이상 착색일 경우에 따라 단풍 판단 여부 결정
# 접근 : 8장 이상 -> Yes, 그 외 -> No
n = int(input())

if n >= 8:
    print("Yes")
else:
    print("No")