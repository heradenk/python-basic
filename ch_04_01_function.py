def add(a, b):
    return a + b


def say():
    return 'Hi'
a = say()
print(a)


def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3, 4)


def say():
    print('Hi')
say()


def add(a, b):
    return a+b
result = add(a=3, b=7)
print(result)


def add_many(*args):    # 여러 
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)


def print_kwargs(**kwargs): # 키워드 파라미터
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo', age=3)


def add_and_mul(a,b):
    return a+b, a*b
result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용", 27)
say_myself("박응선", 27, False)


a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

def vartest(a):
    a = a + 1
vartest(3)
print(a)


a = 1 		    # return
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)

a = 1 		    # global					
def vartest():
    global a
    a = a+1
vartest()
print(a)


add = lambda a, b: a+b
result = add(3, 4)
print(result)

def add(a, b):
    return a+b
result = add(3, 4)
print(result)
