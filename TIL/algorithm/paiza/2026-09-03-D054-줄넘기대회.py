# 문제 : 올해 기록이 작년 기록을 초과했는지 여부 결정
# 접근 : 작년 기록A, 올해 기록B
#       올해 기록이 작년 기록 초과 -> Yes
#       올해 기록이 작년 기록과 같거나 미만 -> No
A,B = map(int, input().split())
if A < B:
    print("Yes")
else:
    print("No")