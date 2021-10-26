# Q1

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# Q2    # +=
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: 
        result += i
    i += 1
print(result)

# Q3    
number = 0
while number < 5:
    number = number + 1
    print('*' * number)

# Q4
for i in range(1,101):
    print(i)

# Q5    # +=
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total_score = 0
for i in score:
    total_score += i
average = total_score / len(score)
print(average)
    
# Q6   # [표현식 for 항목 in 반복가능객체 if 조건문] 
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)
