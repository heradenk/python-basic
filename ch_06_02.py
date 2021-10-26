# 내 풀이
#i = 1
#i< 1000
#if i%3 == 0:
    #result.append(i)
 #   i = i + 1
#elif i%5 == 0:
    #result.append(i)
 #   i = i + 1
#else:
 #   i = i + 1
# print(result)

# 책풀이
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)
        
