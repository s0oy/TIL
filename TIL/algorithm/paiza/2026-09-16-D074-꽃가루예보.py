# 문제 : 꽃가루 양에 따른 외출 여부
# 접근 : 10일 중 꽃가루 양이 2이면 외출 가능
# 막힌점 : count = ~ -> 꽃가루 수치가 2이하인 날을 발견할 때마다
#                      1을 세어서 모두 더함
po_list = list(map(int, input().split()))

count = sum(1 for x in po_list if x <= 2)

print(count)