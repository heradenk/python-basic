import sys

option = sys.argv[1] # sys.argv[0]은 파일 이름 

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a') # 옵션이 a인 경우 입력
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':	      # 옵션이 v인 경우 출력 
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
