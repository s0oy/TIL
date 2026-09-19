# 문제 : 합계 금액에 따라 할인 여부 결정
# 접근 : p엔 음식과 q엔 음료 부탁했을 때 
#       합계 금액 1000엔 이상이면 100엔 할인
p = int(input())
q = int(input())

price = p + q

if price >= 1000:
    print(price - 100)
else:
    print(price)