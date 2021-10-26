print("=" * 50)
print("My Program")
print("=" * 50)


print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
print("Error is %d%%." % 98)


print("%10s" % "hi")         # %10s는 공백10칸, 오른쪽 정렬
print("%-10sjane." % 'hi')   # -10s는 왼쪽 정렬
print("%0.4F" % 3.42134234)  # 넷째자리까지
print("%10.4f" % 3.42134234) # 공백, 넷째 자리 까지만

print("i eat {0} apples".format(3))
print("i eat {0} apples".format("five"))
number = 3
print("i eat{0} apples.".format(number))
number = 3
day = "Three"
print("i ate {0} apples. so i was sick for {1} days.".format(number, day))
print("I ate {number} apples. so i was sick for {day} days.".format(number=10, day=3))

print("{0:<10}".format("hi"))   # 왼쪽 정렬
print("{0:>10}".format("hi"))   # 오른쪽 정렬
print("{0:^10}".format("hi"))   # 가운데 정렬
print("{0:=^10}".format("hi"))  # 공백 채우기
print("{0:!<10}".format("hi"))  # 공백 채우기
y = 3.42134234
print("{0:10.4f}".format(y))    # 소수점 표현
print("{{ and }}".format())     # {} 문자 표현


name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')   # f 문자열 포매팅
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.') # 딕셔너리 포매팅

print(f'{"hi":<10}')    # 왼쪽 정렬
print(f'{"hi":>10}')    # 오른쪽 정렬
print(f'{"hi":^10}')    # 가운데 정렬
print(f'{"hi":=^10}')   # 가운데 정렬 공백채우기
print(f'{"hi":!<10}')

y = 3.42134234
print(f'{y:0.4f}')      # 소수점 표현
print(f'{y:10.4f}')     # 소수점 4자리, 10자리수로 맞춤
print(f'{{ and }}')     # {} 표현

a = "hobby"
print(a.count('b'))     # 문자(b) 개수 세기

a = "Python is the best choice"
print(a.find('b'))      # 위치 알려주기

a = "Life is too short"
print(a.index('t'))     # 위치 알려주기

print(",".join('abcd')) # 문자열 삽입
print(",".join(['a','b','c','d']))

a = "hi"
print(a.upper())        # 대문자로 바꾸기
a = "HI"
print(a.lower())        # 소문자로 바꾸기

a = " hi "              
print(a.lstrip())       # 왼쪽 공백 지우기
a = " hi "
print(a.rstrip())       # 오른쪽 공백 지우기
a = " hi "              
print(a.strip())        # 양쪽 공백 지우기

a = "Life is too short"
print(a.replace("Life", "Your leg"))   # 문자열 바꾸기

a = "Life is too short"
print(a.split())                       # 문자열 나누기
b = "a:b:c:d"
print(b.split(':'))
