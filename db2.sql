show databases;

use t1;

show tables;

desc sungjuck;

select sum(kor), avg(kor), count(kor), count(*)
from sungjuck;

select hak, sum(kor), avg(kor), count(kor), count(*)
from sungjuck
group by hak;

select hak, ban, sum(kor), avg(kor), count(kor), count(*)
from sungjuck
group by hak, ban;

-- =================================================
-- having
select hak, sum(kor), avg(kor)
from sungjuck
where hak=1
group by hak;

-- having:  group이 된 자료에다가 조건을 달아줄때 쓰임
-- where 절과의 차이점은 where은 조건으로 추린후 그룹핑  having 그룹으로 나눈 후 조건절이 붙어짐
select hak, sum(kor), avg(kor)
from sungjuck
group by hak
having hak=1;
-- ======================================
select hak, ban, sum(kor), avg(kor)
from sungjuck
group by hak, ban;

select hak, ban, sum(kor), avg(kor)
from sungjuck
group by hak, ban
having hak =1 and ban =1;

select hak, ban, sum(kor), avg(kor)
from sungjuck
where hak =1 and ban =1
group by hak, ban;

select hak, ban, sum(kor), avg(kor)
from sungjuck
group by hak, ban
having sum(kor) >= 100;


-- 데이터를 정확하고 일관성있게 보관하는것 = 데이터 무결성 - > 테이블을 분리해서 연결
-- join
use employees;
show tables;

desc employees;
desc dept_emp;
desc departments;
desc salaries;

-- employees 와 dept_emp 의 emp_no 값을 조인 시키기 
-- inner join : 해당하는 값이 같은 것만 연결시켜 해당 값만 보여줌=> 해당안하는 값을 보여주는것 - outer join 
select e1.emp_no, first_name, last_name, dept_no, from_date, to_date
from employees e1 inner join dept_emp de -- from에서 테이블명 한칸띄워서 별칭가능
on e1.emp_no = de.emp_no;

-- 연결된 employees 와 dept_emp   + department 연결해서 3개의 테이블 연결 ! 
select e1.emp_no, first_name, last_name, de.dept_no, from_date, to_date
from employees e1 inner join dept_emp de -- from에서 테이블명 한칸띄워서 별칭가능
on e1.emp_no = de.emp_no inner join departments -- 끝나는 지점에서 inner join으로 통체로 연결
on de.dept_no = departments.dept_no;

-- Finance에 근무하는 사원의 사원번호, 이름, 입사일
-- 부서명을 출력하시오

show tables;
desc current_dept_emp;
desc dept_emp; -- 사원번호, 부서코드, from , to
desc dept_manager; -- 관리자 , 부서코드, 사원코드
desc departments; -- 부서명 , 부서코드
desc salaries; -- 사원번호, 급여

select employees.emp_no, employees.first_name, hire_date, dept_name
from employees inner join dept_emp
on employees.emp_no = dept_emp.emp_no inner join departments
on dept_emp.dept_no = departments.dept_no
where dept_name = 'finance';

-- Marketing 부서 관리자의 사원번호, 이름, 입사일을 출력하시오.
select *
from departments;

select employees.emp_no, employees.first_name, hire_date, dept_name
from departments inner join dept_emp
on departments.dept_no = dept_emp.dept_no inner join employees
on dept_emp.emp_no = employees.emp_no inner join dept_manager
on employees.emp_no = dept_manager.emp_no
where dept_name = 'Marketing';

-- 1985년에 입사한 사원의 사원번호, 이름 입사일 급여 부서명을 출력하시오
select employees.emp_no, first_name,hire_date, dept_name,salary, salaries.from_date, salaries.to_date
from employees inner join dept_emp
on employees.emp_no = dept_emp.emp_no inner join departments
on dept_emp.dept_no = departments.dept_no inner join salaries
on dept_emp.emp_no = salaries.emp_no
where hire_date like '1985%';

-- 급여가 75000 이상 받 사원의 사원번호 이름 급여 입사일을 출력하시오
select employees.emp_no, first_name, salary
from employees inner join salaries
on employees.emp_no = salaries.emp_no
where salaries.salary >= 75000;

select *
from salaries;

-- 서브쿼리
select * from employees;

select * from dept_emp;
select * from departments;

-- 부서코드가 'd003'인 사원의 사원번호, 이름, 성별을 출력하시오.
select employees.emp_no, first_name, gender
from employees inner join dept_emp
on employees.emp_no = dept_emp.emp_no
where dept_emp.dept_no = 'd003';

select emp_no, first_name, gender
from employees 
where	emp_no in(
	select emp_no
	from dept_emp
	where dept_no='d003');
    -- 2개 이상일때는 in 이라는 것을 써줌
-- 급여가 60098이고 from date = '2000-08-02' and to_date '2001-08-92 에 해당하는 사원의 번호, 이름, 입사일 출력

select employees.emp_no, first_name, hire_date
from employees inner join salaries
on employees.emp_no = salaries.emp_no
where salary = 60098 and from_date='2000-08-02' and to_date= '2001-08-02';
-- 10006

select emp_no, first_name, hire_date
from employees
where emp_no =(
	select emp_no
	from salaries
	where salary = 60098 and from_date='2000-08-02' and to_date= '2001-08-02');
 
 
 
 -- 평균 급여보다 많이 받는 ..
select avg(salary)
from salaries;

select employees.emp_no, first_name, hire_date
from employees inner join salaries
on employees.emp_no = salaries.emp_no
where salary>(
select avg(salary)
from salaries);
            
-- 부서별 평균급여보다 많이받는 사원의 사원번호 이름 급여 성별 출력 
 desc dept_emp;
 desc salaries;
 
-- 부서별 평균급여 
select dept_no, avg(salary)
from employees inner join salaries
on employees.emp_no = salaries.emp_no inner join dept_emp
on employees.emp_no = dept_emp.emp_no
group by dept_emp.dept_no;

-- 부서별 평균보다 높은
select employees.emp_no, first_name, hire_date, salary, d1.dept_no
from employees inner join salaries
on employees.emp_no = salaries.emp_no inner join dept_emp d1
on employees.emp_no = d1.emp_no
where salary>(
	select avg(salary)
	from employees inner join salaries
	on employees.emp_no = salaries.emp_no inner join dept_emp d2
	on employees.emp_no = d2.emp_no 
    where d1.dept_no = d2.dept_no -- 서브쿼리에서 부서가 같은지 확인(싱크)
	group by d2.dept_no	) limit 0,15;  -- 양이 많아서 리미트로

-- from절안에서 서브쿼리
select e.*
from (
	select emp_no, first_name, hire_date
    from employees
    where emp_no<=10010

	) e;

-- select 안에서 서브쿼리
select emp_no, first_name, hire_date,
	(select avg(salary) from salaries)     
from employees
limit 0,20;

-- 별칭 넣은 서브쿼리
select empno, fname, sal, lname
from (
	select employees.emp_no as empno, first_name as fname, salary as sal, last_name as lname
	from employees join salaries
	on employees.emp_no=salaries.emp_no
	where employees.first_name like 'A%'
) tb1 limit 0,20;

-- 테이블 생성
show databases;
use t1;

create table sample
(
	no int
	, name varchar(10)
    , age int 
    , addr varchar(50)
    

);
-- 자료추가하기 insert into 테이블명 values(로우값들 )
desc sample;
insert into sample values(1,'hong',20,'seoul');
insert into sample(no, name) values(2,'park'); -- 특정 값만 집어넣을때
insert into sample values(1,null,20,'seoul');

select *
from sample;


insert into sample(name, age)
values('test', 20);
-- 자동으로 증가 auto_increment
/* 제약조건
 primary key 제약조건
 foreign key 제약조건
 not null 제약조건
 unique 제약조건
 check 제약조건
 */
create table member1(
	member_id int primary key auto_increment
    , name varchar(20) not null -- null값은 허용 안함
    , age int check(age >=0 and age <=150) -- check 조건절인듯
    , addr varchar(30)
    );

insert into member1(name, age, addr) values('홍', 10, '서울');
insert into member1(name, age) values('박', 20);

select * from member1;

insert into member1(age, addr) values(20, '제주'); -- name 필드에 not null 때문에 오류 발생
insert into member1(name, age) values('hi',200); -- check 조건에 의해서 오류발생!

-- column 집어넣는법
alter table member1
	add jumsu int not null default 0; -- default 0 -> 입력을 안했을때 기본값 설정

select * from member1;

insert member1(name, age) values('aaa', 15);

-- 데이터 변경

commit;

select * from member1;

update member1
set 
	name = '김하나'
    ,age = 20
    ,addr = '제주'
where member_id = 1;   -- 주의) where 절을 안쓰면 전체가 변경

-- 데이터 삭제 
show tables;
select * from member1;

delete  -- delete는 row(행) 정보를 삭제함 < = > select는 colums(열) 정보를 가져옴
from member1
where member_id = 1;

-- 1. employees 데이터 베이스에 저장되어 있는 테이블을 쓰시오.
use employees;
show databases;
-- 답)employees information_schema mysql performance_schema sys t1

-- 2. employees 테이블의 컬럼과 각각의 자료형, 제약조건을 찾으시오.
desc employees;
-- 답) emp_no(int, primary, not null), birth_date(date), first_name(varchar(14)), last_name(varchar(16)),
--    gender(enum('M','F'), hire_date(date)

-- 3. first_name에 문자 A 포함되는 사원의 사원번호, 이름 , 입사일을 출력하시오.
select emp_no, first_name, hire_date
from employees
where first_name like '%A%';

-- 4. first_name에 끝에서 두번째 글자가 E인 사원의 사원번호, 이름 , 급여, 부서명을 출력하시오.
show tables;
desc dept_emp; -- 사원번호, 부서코드, from , to
desc dept_manager; -- 관리자 , 부서코드, 사원코드
desc departments; -- 부서명 , 부서코드
desc salaries; -- 사원번호, 급여
-- em - 
select employees.emp_no, first_name, salary, dept_name
from employees inner join salaries
on employees.emp_no = salaries.emp_no join dept_emp
on salaries.emp_no = dept_emp.emp_no join departments
on dept_emp.dept_no = departments.dept_no
where first_name like '%E_';


-- 5. 급여를 많이 받는 사원의 사원번호 이름 급여 부서명을 출력하시오.
desc dept_emp; -- 사원번호, 부서코드, from , to
desc dept_manager; -- 관리자 , 부서코드, 사원코드
desc departments; -- 부서명 , 부서코드
desc salaries; -- 사원번호, 급여

select employees.emp_no, first_name, salary, dept_name
from employees inner join salaries
on employees.emp_no = salaries.emp_no join dept_emp
on salaries.emp_no = dept_emp.emp_no join departments
on dept_emp.dept_no = departments.dept_no
where salary = (
select Max(salary)
from salaries);

-- 6. 평균급여보다 많이 받는 사원의 사원번호, 이름, 급여, 입사일을 출력하시오.
select employees.emp_no, first_name, salary, hire_date
from employees inner join salaries
on employees.emp_no = salaries.emp_no
where salary>(
select avg(salary)
from salaries);

-- 7. 남자 평균 급여와 여자 평균 급여를 출력하시오.  -- 젠더 값은 employees 테이블에만 존재

select gender, avg(salary)
from salaries inner join employees
on salaries.emp_no = employees.emp_no
group by gender;


-- 8. 각 성별로 평균급여 보다 많이 받는 사원의 상위 5명의 이름과 급여 입사일 부서명을 출력하시오.
-- 남자
select employees.emp_no, first_name, max(salary), hire_date, dept_name
from employees inner join salaries
on employees.emp_no = salaries.emp_no inner join dept_emp
on salaries.emp_no = dept_emp.emp_no inner join departments
on dept_emp.dept_no = departments.dept_no
where salary > (
	select avg(salary)
	from salaries    
    ) and gender ='M' -- 'F'로 바꾸면 여자 데이터 출력
group by emp_no
order by max(salary) desc
limit 0,5;


	
