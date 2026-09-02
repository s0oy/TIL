# 문제 : 성적에 따라 선물 결정
# 접근 : 성적이 3 -> 가장 비싼 것, 2 -> 2번째로 비싼 것, 1 -> 가장 저렴한 것
g = int(input())
p_1, p_2, p_3 = input().split()
if g == 3:
    print(p_3)
elif g == 2:
    print(p_2)
else:
    print(p_1)