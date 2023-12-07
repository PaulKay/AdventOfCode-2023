import re

f = open('Day2_input.txt')
# number of cubes revealed by elf (red, green, blue)
numCubes = [12,13,14]

sumIDs = 0
for line in f:
    numbers = re.findall(r'\d+', line)
    print("Game",numbers[0])
    ixStart = line.index(':')+1
    ixPick = [i for i, x in enumerate(line) if x == ';']
    ixPick.append(-1)

    notPossible = 0
    possible = 0
    for ix in ixPick:
        pick = line[ixStart+1:ix]
        #print(pick)
        ixStart = ix+1
        # process the pick
        numbersPick = re.findall(r'\d+', pick)
        colours = re.findall(r'\D+', pick)

        sumRed = 0
        sumGreen = 0
        sumBlue = 0

        for number, colour in zip(numbersPick,colours):
            if "red" in colour:
                sumRed = sumRed + int(number)
            elif "green" in colour:
                sumGreen = sumGreen + int(number)
            elif "blue" in colour:
                sumBlue = sumBlue + int(number)
        #print('Sum Red', sumRed, ',Sum Green', sumGreen, ',Sum Blue', sumBlue)
        if sumRed <= numCubes[0] and sumGreen <= numCubes[1] and sumBlue <= numCubes[2]:
            possible = possible + 1
        else:
            notPossible = notPossible + 1
    if notPossible is 0:
        sumIDs = sumIDs + int(numbers[0])
            
    
    
print('Sum IDs', sumIDs)