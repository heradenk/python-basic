# Q1

def is_odd(a):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")	# is_odd = lambda x: True if x % 2 == 1 else False
    
# Q2

def avg(*args):
    result = 0
    for i in args:
        #result += i
    return result / len(args)
    
# Q3

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = #int(input1) + #int(input2)
print("두 수의 합은 %s 입니다" % total)

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
#f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
#f2.close()

# Q6
#user_input = input("저장할 내용을 입력하세요:")
f = open("test.txt", 'a')
f.write(user_input)
#f.write("\n")
f.close()

# Q7
#f = open("test.txt", 'r')
#body = f.read()
f.close()

#body = body.replace('java', 'python')

#f = open('test.txt', 'w')
#f.write(body)
f.close()
