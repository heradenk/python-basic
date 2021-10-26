f = open("C:/새파일.txt", 'w')
f.close()

f = open("C:/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)

f = open("C:/새파일.txt", 'r')
line = f.readline()	# 첫째줄 읽기
print(line)
f.close()

f = open("C:/새파일.txt", 'r')
while True:		# 모든줄 읽기
    line = f.readline()
    if not line: break
    print(line)
f.close()

while True:
    data = input()
    if not data: break
    print(data)


f = open("C:/새파일.txt", 'r')
lines = f.readlines()	# readlines 리스트
for line in lines:	# line = line.strip() 줄바꿈 제거
    print(line)
f.close()

f = open("C:/새파일.txt", 'r')
data = f.read()
print(data)
f.close()


f = open("C:/새파일.txt", 'a') # 새로운 내용 추가
for i in range(11, 20):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()


with open("foo.txt", "w") as f: # with문
    f.write("Life is too short, you need python")
    
