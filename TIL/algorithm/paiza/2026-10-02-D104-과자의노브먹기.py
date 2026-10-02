# 문제 : 노브를 먹은 후에 남아있는 과자의 수 출력
# 접근 : 과자 n개에서 각각 a개, b개만 먹었기에 뺌
n = int(input())
a = int(input())
b = int(input())
print(n - a - b)