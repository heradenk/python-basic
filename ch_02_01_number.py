a = [1 ,2 , 3, ['a', 'b','c']]          # 인덱싱
print(a[-1][0])
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])


a = [1, 2, 3, 4, 5]                     # 슬라이싱
print(a[0:2])
a = "12345"
print(a[0:2])
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

a = [1, 2, 3]
print(str(a[2]) + "hi")     # (a[2] + "hi") 오류 해결 

a = [1, 2, 3]
a[2] = 4        # 리스트 값 수정      
print(a)        

a = [1, 2, 3]
del a[1]
print(a)        # 리스트 삭제

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a = [1, 2, 3]
a.append(4)
print(a)         # 리스트 추가
a = [1, 2, 3]
a.append([5, 6])
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)        # 리스트 정렬

a = ['a', 'c', 'b']
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)        # 리스트 뒤집기

a = [1, 2, 3]
print(a.index(3))
print(a.index(1))   # 위치 반환

a = [1, 2, 3]
a.insert(0,4)
print(a)            # 요소 삽입

a = [1, 2 ,3, 1, 2, 3]
a.remove(3)
print(a)            # 요소 제거

a = [1, 2, 3]
print(a.pop(1))     # 요소 끄집어내기
print(a)

a = [1, 2, 3, 1]
print(a.count(1))   # 개수 세기

a = [1, 2, 3]
a.extend([4, 5])
print(a)            # 리스트 확장



