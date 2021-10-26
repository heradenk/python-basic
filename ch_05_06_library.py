import sys
print(sys.argv)
sys.path


import pickle   # 저장
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()
import pickle   # 불러오기
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)


import os           # 시스템 환경
os.environ
os.chdir("C:\WINDOWS")
		    # 디렉터리 위치 변경
os.getcwd()	    # 디렉터리 위치
os.system("dir")    # 명령어 호출
f = os.popen("dir") # 명령어 결과
print(f.read())


import shutil       # 파일 복사
shutil.copy("src.txt", "dst.txt")


import glob         # 디렉터리파일 리스트 만들기
glob.glob("C:/mark*")


import tempfile     # 임시파일 만들기
filename = tempfile.mkstemp()


import time
time.time()	    # 1970년 1월 1일 0시 0분 0초 기준
time.localtime	    # 시간 형태
time.asctime	    # 시간 형태(튜플)
time.ctime	    # 현재 시간
time.strftime	    # 시간 0포맷
time.sleep	    # 시간 간격 주기
import time
for i in range(10):
    print(i)
    time.sleep(1)


import calendar     # 달력 보기
print(calendar.calender(2015))
calendar.weekday(,,)# 요일
calendar.monthrange # 달이 며칠까지 있는지


import random       # 난수
random.random()
random.randint(1, 10)

import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "___main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
data


import webbrowser   # 브라우저 실행
webbrowser.open("http://google.com")

