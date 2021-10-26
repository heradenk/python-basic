result = 0

def add(num):		# 더하기
    global result
    result += num
    return result

print(add(3))
print(add(4))


result1 = 0
result2 = 0

def add1(num):		# 더하기 두개
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


class Calculator:	# 클래스, 빼기 
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class Cookie:		# 껍질
    pass

a = Cookie()		# 객체 만들기
b = Cookie()


# 사칙연산 만들기
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):	# 메서드 
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4,2)	    # 객체 만들기
b = FourCal(3,8)
a.setdata(4, 2)	    # 데이터 지정
b.setdata(3, 8)
print(a.add())	    # 더하기
print(b.add())
print(a.mul())	    # 곱하기
print(b.mul())
print(a.sub())	    # 빼기
print(b.sub())
print(a.div())	    # 나누기
print(b.div())


class MoreFourCal(FourCal):	# 클래스 상속
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4, 2)
print(a.pow())


class SafeFourCal(FourCal):	# 메서드 오버라이딩(덮어쓰기)
    def div(self):
        if self.second == 0:	# 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

class Family:
    lastname = "김"
a = Family()
b = Family()
print(Family.lastname)
print(a.lastname)
print(b.lastname)
