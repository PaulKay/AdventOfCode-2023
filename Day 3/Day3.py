import re
import math

f = open('input.txt')
characters = [chr(i) for i in [33,34,35,36,37,38,39,40,41,42,43,44,45,47,58,59,60,61,62,63,64]]
numbers = [chr(i) for i in range(48,58)]

lines = []
characters_center = []
characters_found = []
numbers_found = []
for row, line in enumerate(f):
    character_line = []
    character_center = []
    numbers_line = []
    for column, char in enumerate(line):
        if char in characters:
            character_line.append(column)
            character_center.append(char)
        if char in numbers:
            numbers_line.append(column)
    characters_found.append(character_line)
    characters_center.append(character_center)
    numbers_found.append(numbers_line)
    lines.append(line)
            
nRows = len(characters_found)
nColumns = len(line)

numbers_adjacent_row = []
numbers_adjacent_col = []
center = []

angles = [0,45,90,135,180,225,270,315]
# find all the single digits which are adjacent to the found characters
for row in range(nRows):
    print('row',row)
    for char,col in zip(characters_center[row],characters_found[row]):
        print('character center', char, col)
        for theta in angles:
            x = round(math.cos(math.radians(theta)))
            y = round(math.sin(math.radians(theta)))
            row_search = row + y
            col_search = col + x
            #print(row_search,col_search)
            if row_search<=139 and row_search>=0 and col_search<=139 and col_search>=0:
                if col_search in numbers_found[row_search]:
                    numbers_adjacent_row.append(row_search)
                    numbers_adjacent_col.append(col_search)
                    center.append(char)
                    #print(char,lines[row][col])
                    

maxDigitLength = 5
# for all digits found, find the associated full number
digits_location = []
digits_found = []
for char,row,col in zip(center,numbers_adjacent_row, numbers_adjacent_col):
    number_adjacent = lines[row][col]
    for i in range(1,maxDigitLength):
        if lines[row][col+i] in numbers and col+i<=139:
            number_adjacent = number_adjacent + lines[row][col+i]
        else:
            break
    for i in range(1,maxDigitLength):
        if lines[row][col-i] in numbers and col-i>=0:
            number_adjacent = lines[row][col-i] + number_adjacent
        else:
            number_col = col-i
            break
    digit_location = [number_adjacent, row, number_col]
    if digit_location not in digits_location:
        digits_location.append(digit_location)
        digits_found.append(int(number_adjacent))
        #print(row, number_col, char,number_adjacent)

sum_digits = sum(digits_found)
print(sum_digits)
    