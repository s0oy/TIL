# 문제 : A 군주거래로 손해인지 얻었는지 출력 
# 접근 : a이 거래에서 얻은 경우 -> yes, 손실된 경우 -> no
a = int(input())
b = int(input())
if b >= a:
    print("Yes")
else:
    print("No")