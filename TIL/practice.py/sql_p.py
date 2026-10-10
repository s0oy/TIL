# SQL 기초

# DB에서 데이터를 조회하고 관리할 때 사용하는 언어

# 문법 예제
# 이 쿼리는 판매기록과 품목정보를 연결한 뒤, 
# 품목별 평균가격과 총판매량 계산하고 평균가격이 높은 순으로 정렬 
SELECT
    p.product_name,
    AVG(s.price) AS average_price,
    SUM(s.quantity) AS total_quantity
FROM sales AS s
JOIN products AS p
    ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY average_price DESC;


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


SELECT : 가져올 열 지정
WHERE : 그룹화 전 행 필터링
JOIN : 여러 테이블 결합
AND : 두 조건 모두 만족
OR : 둘 중 하나 이상 만족
ORDER BY : 정렬
GROUP BY : 그룹별 집계
DESC : 내림차순
ASC : 오름차순
HAVING : 집계한 그룹 필터링
LIMIT : 결과 개수 제한


# 3. WHERE와 HAVING의 차이

# 개별 행 먼저 필터링
-- 가격이 3000 이상인 기록만 그룹화
SELECT product_id, AVG(price)
FROM sales
WHERE price >= 3000
GROUP BY product_id;

# 그룹별 계산 후 결과 필터링
-- 평균 가격이 3000 이상인 그룹만 출력
SELECT product_id, AVG(price)
FROM sales
GROUP BY product_id
HAVING AVG(price) >= 3000;


# 4. 그룹별 평균
# Pandas의 groupby()와 비슷한 역할 함

SELECT study_hours, AVG(score) AS average_score
FROM students
GROUP BY study_hours;


# 5. Pandas와 SQL 비교
작업	   |          Pandas	   |            SQL
데이터 조회	|  df[["이름", "점수"]]	 |  SELECT name, score FROM students;
조건 필터링	|  df[df["점수"] >= 80]	|   WHERE score >= 80
정렬	   |  sort_values()	       |  ORDER BY
그룹 평균   |  groupby().mean()    |   GROUP BY + AVG()