# Q1 평균
a = 80
b = 75
c = 55
average = (a + b + c)/3
print(average)

# Q2 홀짝

A.%를 이용한다

# Q3 슬라이싱
number = '881120-1068234'
print(number[0:6])
print(number[7:14])

# Q4 출력
pin = "881120-1068234"
print(pin[7])

# Q5 replace
a = "a:b:c:d"
print(a.replace(":", "#"))

# Q6 역순
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7 합
a = ['Life', 'is', 'too', 'short']
print(a[0] + a[1] + a[2] + a[3])

A. "".join(a)

# Q8 추가
a = (1, 2, 3)
b = (4,)
a = a + b
print(a)

# Q9 오류 찾기
#1. a['name'] = 'python'
#2. a[('a',)] = 'python'
#3. a[[1]] = 'python'
#4. a[250] = 'python'

3

# Q10 추출
a = {'A':90, 'B':80, 'C':70}
print(a.get('B'))
A. get => pop

# Q11 중복 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
