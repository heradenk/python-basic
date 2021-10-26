abs(3)		 # 절댓값


all([1, 2, 3]) 	 # 자료형 참, 거짓 and
all([1, 2, 3, 0])
all([])


any([1, 2, 3, 0])# 자료형 참, 거짓 or
any([0, ""])
any([])


chr(97)	     	# 유니코드 문자 출력
chr(44032)


dir([1, 2, 3])	# 관련 메서드 보여주기
dir({'1':'a'})


divmod(7, 3) 	# a를 b로 나눈 몫, 나머지

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
	     	# 열거, 인덱스값


eval('1+2')	# 실행
eval("'hi' + 'a'")
eval('divmod(4, 3)')


#positive.py	# 필터
def positive(1):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
print(positive([1, -3, 2, 0, -5, 6]))


#filter1.py
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))


hex(234)	# 16진수
hex(3)


a = 3   	# 주소
id(3)
id(a)
b = a
id(b)


a = input()	# 입력
a
b = input("Enter: ")
b


int('3')	# 정수 
int('3.4')
int('11', 2)	# 2진수
int('1A', 16)	# 16진수


class Person: pass
a = Person()	# 인스턴스 확인
isinstance(a, Person)


len("python")	# 길이
len([1,2,3])


list("python")	# 리스트 만들기 
list((1,2,3))


# two_times.py	# 함수
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1, 2, 3, 4])
print(result)

def two_times(x):
    return x*2
list(map(two_times, [1,2,3,4]))

list(map(lambda a: a*2, [1, 2, 3 ,4]))


max([1, 2, 3])	# 최댓값
max("python")


min([1, 2, 3])	# 최솟값
min("python")


oct(34)		# 8진수 문자열
oct(12345)

		# 파일이름, 읽기방법
f = open("binary_file", "rb")
fread = open("read_mode.txt", 'r')
fread2 = open("read_mode.txt")
fappend = open("append_mode.txt", 'a')


ord('a')	# 문자의 유니코드 값
ord('가')


pow(2, 4)	# 제곱
pow(3, 3)


list(range(5))	# 범위값 세번째는 숫자 사이의 거리
list(range(5, 10))
list(range(1, 10, 2))


round(4.6)	# 반올림
round(4.2)

		# 정렬
sorted([3, 1, 2])
sorted(['a', 'c', 'b'])
sorted("zero")
sorted((3, 2, 1))


str(3)		# 문자열 
str('hi')
str('hi'.upper())


sum([1,2,3])	# 합
sum((4,5,6))


tuple("abc")	# 튜플로
tuple([1,2,3])
tuple((1,2,3))


type("abc")	# 자료

		# 자료형 묶기
list(zip([1,2,3], [4,5,6]))
list(zip([1,2,3], [4,5,6], [7,8,9]))
list(zip("abc", "def"))
