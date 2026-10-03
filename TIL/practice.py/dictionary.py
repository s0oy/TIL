# 딕셔너리
# key : value 구조
student = {
    "name" : "명수",
    "age" : 19,
    "major" : "IT"
}

print(student["name"])   # 명수

# 값 변경
student["age"] = 21

# 추가
student["language"] = "Japanese"

# 문제1
# 다음 정보를 딕셔너리로 만들기
# 이름: So, 전공: 융합계열, 공부: Python, 목표: 일본 IT 취업
student = {
    "name" : "영자",
    "major" : "IT",
    "study" : "Python",
    "obj" : "일본 IT 취업" 
}

# 문제2
# 목표 값 출력
student = {
    "name" : "영자",
    "major" : "IT",
    "study" : "Python",
    "obj" : "일본 IT 취업" 
}

print(student["obj"])   # 일본 IT 취업