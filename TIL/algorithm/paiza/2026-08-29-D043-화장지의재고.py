# 문제 : 나머지가 n롤 이하가 되었을 때 m롤 매입
# 접근 : 매수하는 기준의 롤수n, 매수하는 롤수m, 현재의 롤수x
#       x가 n롤 이하면 x + m
n = int(input())
m = int(input())
x = int(input())
if x <= n:
    x += m
print(x)
