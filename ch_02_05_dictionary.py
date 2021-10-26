# key 와 value

a = {1: 'a'}    # 딕셔너리 추가
a[2] = 'b'
print(a)

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys()) # key 리스트 만들기

for k in a.keys():
    print(k)

print(list(a.keys()))

print(a.values())   # value 리스트 만들기
print(a.items())    # key,value 쌍 얻기

a.clear()           # key, value 쌍 지우기
print(a)

a = {'name':'pey', 'phone':'011999323', 'birth': '1118'}
print(a.get('name')) # key로 value 얻기
print(a.get('phone'))

a = {'name':'pey', 'phone':'011993323', 'birth': '1118'}
print('name' in a)   # 해당 key가 딕셔너리 안에 있는지 조사
print('email' in a)
