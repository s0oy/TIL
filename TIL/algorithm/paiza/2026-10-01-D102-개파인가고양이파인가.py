# 문제 : 3명의 설문조사 중 2명 이상이 대답한 쪽 출력
# 접근 : 읽어온 3개의 단어가 animal 리스트에 저장,
#       .count -> 리스트에 문자열이 총 몇 개 들어있는지 갯수 셈
animal = [input().strip() for _ in range(3)]

if animal.count("cat") >= 2:
    print("cat")
else:
    print("dog")