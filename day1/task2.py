import re

def convert(a: str, reverse: bool) -> int:
    num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if str(a).isdigit(): # if it's a digit, we can just cast
        return int(a)
    else:
        if reverse:
            return num_words.index(a[::-1]) # 0 is not mentioned in task but
                                            # including it allows us to just do this
        else:
            return num_words.index(a)

x = open(file = "day1/input.txt")
sum = 0
lines = x.readlines()

for line in lines:
    list = re.findall("\d{1}|one|two|three|four|five|six|seven|eight|nine", line) # one digit or word representation
    d1 = convert(list[0], False)
    # due to re shaboingery I can't get last value if it begins in previous match
    # so just reverse everything LOL
    list2 = re.findall("\d{1}|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno" , line[::-1]) 
    d2 = convert(list2[0], True)
    sum = sum + 10*d1 + d2

print(sum)
