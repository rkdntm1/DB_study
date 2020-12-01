use employees;
select * from employees limit 0,10;
-- 0,10 -> 0이 1 / 0을 시작으로해서 10개 보여주세요 라는말

-- select 다음에는 선택할 항목을 씁니다.
select * from employees limit 10,5;
select emp_no, first_name,last_name from employees limit 10,5;

-- 중복값 제거 해보기(distinct)
select gender from employees limit 10, 20;
select distinct gender from employees;

-- where
select * from employees where emp_no=100001;
desc employees;
select emp_no, first_name, last_name, gender from employees where emp_no =10005;

-- 이름 합치기(concat) , as (별명 붙이기)
select emp_no, concat(first_name,' ',last_name) as full_name from employees where emp_no = 10005;

-- 사원번호가 10010이항힌 사원의 사원번호, 이름, 성, 입사일을 출력하시오.
select emp_no,first_name, last_name, hire_date from employees where emp_no <= 10010;

-- 입사일이 '1989-09-12'인 사원의 사원번호, 이름, 입사일을 출력하시오.
select emp_no, first_name, hire_date from employees where hire_date = '1989-09-12';

-- 이름이 Gio 인 사원의 사원번호 이름 성별을 출력하시오
select emp_no, first_name, gender from employees where first_name = 'Gio';

-- between 연산자 와 >= and <= 사용
-- 사원번호가 10010이상이고 10020이하인 사원의 사원번호, 이름 , 생년월일을 출력하시오
select emp_no, first_name, birth_date from employees where emp_no >=10010 and emp_no<=10020;
select emp_no, first_name, birth_date from employees where emp_no between 10010 and 10020;
-- between 연산자는 앞의 숫자가 뒤에 숫자보다 작아야 함 
select emp_no, first_name,birth_date from employees where emp_no between 10020 and 10010;	

-- 1985-02-02 일 부터 1985-02-05에 입사한 사원의 사원번호 이름 입사일 출력 
-- order by (오름차순 정렬하기) , 맨뒤 desc 하면 내림차순
select emp_no, first_name, hire_date from employees where hire_date between '1985-02-02' and '1985-02-05' order by hire_date;

/*
	사원번호가 10010 이거나 10025 이거나 10030 인 사원의 사원번호, 이름, 입사일, 성별을 출력하시오
    or 연산자와 in 연산자 사용 
*/
select emp_no, first_name, hire_date, gender 
from employees 
where emp_no = 10010 or emp_no = 10025 or emp_no = 10030;

select emp_no, first_name, hire_date, gender 
from employees 
where emp_no in (10010,10025,10030) order by hire_date;

/*
	like
    last_name이 C로 시작하는 사원의 사원번호 이름 입사일 출력
*/
select emp_no, first_name, last_name, hire_date
from employees
where last_name like 'C%' order by first_name;

-- last_name 이 v로 끝나는 사원의 사원번호, 성, 생년월일을 출력
select emp_no, last_name, birth_date
from employees
where last_name like '%v'order by emp_no;

/*
last_name에 v가 포함되는 사원의
사원번호, 이름, 입사일 출력
*/
select emp_no, first_name, hire_date
from employees
where last_name like '%v%';

/*
last_name 끝에서 두번째 글자가 o인 사원의 사원번호 이름 입사일 생년월일 출력
*/
select emp_no, first_name, hire_date, birth_date
from employees
where last_name like '%o_';

/*
last_name에서 전체 4글자중 두번째 글자가 o인 사원의
사원번호 이름 입사일 출력
*/
select emp_no, first_name, hire_date
from employees
where first_name like '_o__';
/*
이름에 o가 포함되는 사원의 사원번호 이름 성별 출력
*/
select emp_no, first_name, gender
from employees
where last_name like '%o%';

-- 
create database t1;
use t1;

create table sungjuck(
id int primary key auto_increment
,name varchar(10)
, kor int
, hak int
,ban int
);
insert into sungjuck(name, kor, hak,ban) values('a',100,1,1);
insert into sungjuck(name, kor,hak,ban) values('b', null,1,1);
insert into sungjuck(name,hak, ban) values('c',1,1);
insert into sungjuck(name,kor, hak,ban) values('d', 50,1,2);
insert into sungjuck(name,kor, hak,ban) values('e', 30,1,3);
insert into sungjuck(name,kor,hak,ban) values('f', 60,2,1);
insert into sungjuck(name,kor,hak,ban) values('g', 70,2,1);
insert into sungjuck(name,kor,hak,ban) values('h', 30,2,2);

commit;

select * from sungjuck;

select id, name, kor, hak, ban
from sungjuck
where kor is null;

-- limit (처음위치, 몇개) , 0은 제일먼저
-- order by --- asc(오름차순,생략가능) , desc(내림차순)  -> 왼쪽부터 정렬 우선순위
select id, name, kor ,hak, ban
from sungjuck
order by hak desc, name asc; -- hak을 먼저 내림차순 정렬하고 거기서 name 값을 오름차순으로 정리

-- ceil(올림)
select ceil(10.2), ceil(10.9), ceil(-10.2), ceil(-10.9)
from dual; -- dual -> 더미 테이블 (테스트용, 계산용)

-- floor(내림)
select floor(10.2), floor(10.9), floor(-10.2), floor(-10.9)
from dual;

-- round(반올림)
select round(10.2), round(10.9), round(-10.2), round(-10.9)
from dual;

-- 아무 계산 가능
select 10+20
from dual;

-- ========================================================
select * from sungjuck;
-- sum avg max min count 
-- count(*) ==> sungjuck 테이블 전체 자료수
-- count(kor) ==> sungjuck 테이블의 kor의 자료수
select sum(kor), avg(kor), max(kor), min(kor)
,count(*), count(kor) from sungjuck;

-- group by
/* 학교단위에서 학년별로 묶기
select
from 학교
group by 학년
*/
desc sungjuck;
/*
	학년별 평균 점수와 최고점수, 최소 점수, 인원을 출력하시오.
*/
select hak, avg(kor), max(kor), min(kor), count(kor)
from sungjuck
group by hak order by hak;

/*
반에 대한 평균, 인원 을 출력하시오.
*/
select ban, avg(kor), count(*)
from sungjuck
group by ban;
-- 학년과 반으로 나눌때
select hak, ban, avg(kor), count(*)
from sungjuck
group by hak, ban;