import re

f = open('Day1_data.txt')
sumAll = 0
for line in f:
    numbers = re.findall(r'\d', line)
    sumDigits_string = numbers[0] + numbers[-1]
    sumDigits_int = int(sumDigits_string)
    sumAll = sumAll + sumDigits_int
    print(numbers)
print("Sum of all lines ", sumAll)
f.close()