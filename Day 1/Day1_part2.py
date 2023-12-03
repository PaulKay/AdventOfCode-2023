import re
f = open('Day1_data.txt')
strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_str = [1,2,3,4,5,6,7,8,9]

lineNum = 1
sumAll = 0
for line in f:
    ixAll = []
    numbers = re.findall(r'\d', line)
    first = numbers[0]
    last = numbers[-1]
    first_all = [i for i, x in enumerate(line) if x == numbers[0]]
    last_all = [i for i, x in enumerate(line) if x == numbers[-1]]
    ixFirst = first_all[0]
    ixLast = last_all[-1]
    numbers_found = [line[ixFirst], line[ixLast]]

    ixAll = [ixFirst,ixLast]
    for string in strings:
        if string in line:
            #ixString = line.index(string)
            ixString = [i.start() for i in re.finditer(string, line)]
            ixAll = ixAll + ixString
            ixLen = len(ixString)
            numbers_found = numbers_found + [string]*ixLen
    
    ixMax = max(ixAll)
    ixMin = min(ixAll)

    digit_ix_max = ixAll.index(ixMax)
    digit_ix_min = ixAll.index(ixMin)

    digit_max = numbers_found[digit_ix_max]
    digit_min = numbers_found[digit_ix_min]

    if len(digit_max) > 1:
        digit_max_str = str(strings.index(digit_max)+1)
    else:
        digit_max_str = digit_max
    if len(digit_min) > 1:
        digit_min_str = str(strings.index(digit_min)+1)
    else:
        digit_min_str = digit_min

    digit_line = int(digit_min_str+digit_max_str)
    sumAll = sumAll + digit_line

    print(lineNum, ',', digit_min, digit_max, digit_line,line[0:-1])
    lineNum = lineNum + 1
    # highlight line for troubleshooting
    #line_highlight = line[0:ixMax] + '('+ line[ixMax] + ')' + line[ixMax+1:-1]
    #if ixMax != ixMin:
    #    line_highlight = line_highlight[0:ixMin] + '('+ line_highlight[ixMin] + ')' + line_highlight[ixMin+1:-1]
    #print(line_highlight)
print("Sum of all lines ", sumAll)
f.close()