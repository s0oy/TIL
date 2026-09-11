# 문제 : 총 점수 찾기
# 접근 : 첫 번째 줄에 테스트1,2 점수 / 두번째 줄에 테스트 1의 필요한 최소 점수 주어짐
#       점수a가 필요 최조 점수c 이상일때만 -> 시험2 점수b 합산
#       시험 1점수가 필요 최저 점수 미만 -> 시험1 점수a만 출력
a, b= map(int, input().split())
c = int(input())

if a >= c:
    print(a + b)
else:
    print(a)