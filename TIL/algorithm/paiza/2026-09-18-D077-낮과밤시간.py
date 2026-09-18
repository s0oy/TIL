# 문제 : 길이에 따라 출력 여부 결정
# 접근 : 일이 나오는 시간길이a와 일이 가라앉고 있는 시간길이b가 
#       같은 길이일 경우 -> equinox, 그 외 -> no
a = int(input())
b = int(input())

if a == b:
    print("equinox")
else:
    print("no")