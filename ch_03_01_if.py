money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


money = True                    # or
card =True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print ("걸어가라")


print(1 in [1, 2, 3])           # in
print('a' in ('a', 'b', 'c'))


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")


if 'money' in pocket:           # pass
    pass
else:
    print("카드를 꺼내라")

if 'money' in pocket: pass
else: print("카드를 꺼내라")


pocket = ['paper', 'handphone'] # elif
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
        print("택시를 타고 가라")
else:
        print("걸어가라")


if score >= 60:                 # 간단히
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"
