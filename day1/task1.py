import re

x = open(file = "day1/input.txt")
sum = 0
lines = x.readlines()
for line in lines:
    list = re.findall("\d{1}", line) # find all digits
    d1 = int(list[0]) # first
    d2 = int(list[-1]) # last
    sum = sum + 10*d1 + d2
print(sum)
