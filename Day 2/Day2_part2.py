import re

f = open('Day2_input.txt')
# number of cubes revealed by elf (red, green, blue)
numCubes = [12,13,14]

sumPower = 0
for line in f:
    numbers = re.findall(r'\d+', line)
    print("Game",numbers[0])
    ixStart = line.index(':')+1
    ixPick = [i for i, x in enumerate(line) if x == ';']
    ixPick.append(-1)

    red_picks = []
    green_picks = []
    blue_picks = []
    
    for ix in ixPick:
        pick = line[ixStart+1:ix]
        print(pick)
        ixStart = ix+1
        # process the pick
        numbersPick = re.findall(r'\d+', pick)
        colours = re.findall(r'\D+', pick)

        for number, colour in zip(numbersPick,colours):
            if "red" in colour:
                red_picks.append(int(number))
            elif "green" in colour:
                green_picks.append(int(number))
            elif "blue" in colour:
                blue_picks.append(int(number))
    print('red picks', red_picks, 'green picks', green_picks,'blue picks', blue_picks)
    sumPower = sumPower + max(red_picks)*max(green_picks)*max(blue_picks)
    
print('Sum powers', sumPower)