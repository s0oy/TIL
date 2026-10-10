# SQL 기초

# DB에서 데이터를 조회하고 관리할 때 사용하는 언어

# 1. 기본 조회
-- 모든 데이터
SELECT * FROM students;

-- 이름과 점수만 조회
SELECT name, score
FROM students;

-- 점수가 80점 이상인 학생
SELECT *
FROM students
WHERE score >= 80;

-- 점수 높은 순으로 정렬
SELECT *
FROM students
ORDER BY score DESC;


# 2. 조건을 여러 개 사용
SELECT *
FROM students
WHERE study_hours >= 3
  AND score >= 80;

# WHERE : 조건 지정
# AND : 두 조건 모두 만족
# OR : 둘 중 하나 이상 만족
# ORDER BY : 정렬
# DESC : 내림차순
# ASC : 오름차순


# 3. 그룹별 평균
# Pandas의 groupby()와 비슷한 역할 함

SELECT study_hours, AVG(score) AS average_score
FROM students
GROUP BY study_hours;


# 4. Pandas와 SQL 비교
작업	   |          Pandas	   |            SQL
데이터 조회	|  df[["이름", "점수"]]	 |  SELECT name, score FROM students;
조건 필터링	|  df[df["점수"] >= 80]	|   WHERE score >= 80
정렬	   |  sort_values()	       |  ORDER BY
그룹 평균   |  groupby().mean()    |   GROUP BY + AVG()