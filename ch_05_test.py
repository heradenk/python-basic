# Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

# Q2

class MaxLimitCalculato(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

# Q3
#1. False
#2. True

# Q4
list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))

# Q5
int('0xea', 16)

# Q6
list(map(lambda a: a*3, [1, 2, 3, 4]))

# Q7

list = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(list) + min(list))

# Q8
print(round(17/3, 4))

# Q9
# myargv.py
import sys
numbers = sys.argv[1:]
result = 0
for number in numbers:
    result += int(number)
print(result)

# Q10
import os
os.chdir("c:/doit")
result = os.popen("dir")
print(result.read())

# Q11
import glob
glob.glob("C:/doit/*.py")

# Q12
import time
time.strftime("%Y/%m/%d %H:%M:%S")

# Q13
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)

    if num not in result:
        result.append(num)
print(result)
