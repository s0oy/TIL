# 문제 : 숫자로 된 성적을 알바벳으로 변환 후 성적 출력
# 접근 : 5 -> A, 4 -> B, 3 -> C, 2 -> D, 1 -> E
n = int(input())
if n == 5:
    print("A")
elif n == 4:
    print("B")
elif n == 3:
    print("C")
elif n == 2:
    print("D")
else:
    print("E")