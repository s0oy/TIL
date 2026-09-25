# 문제 : 오전과 오후 강수 확률에 따른 결과값 출력
# 접근 : 오전, 오후 강수량 더한 값이 50이상 -> yes, 그외 -> no
a = int(input())
b = int(input())

if a + b >= 50:
    print("yes")
else:
    print("no")