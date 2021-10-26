a = [1, 2, 3]   # a 메모리 주소
print(id(a))

a = [1, 2, 3]   # 리스트 복사
b = a
print(id(a))
print(id(b))

print(a is b)

a[1] = 4
print(a)
print(b)

a = [1, 2, 3]   # 복사만
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy
a = [1, 2, 3]
b = copy(a)
print(b is a)

a, b = ('python', 'life')   # 변수 만드는 예
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'

