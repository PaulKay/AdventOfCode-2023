import re

f = open('input.txt')
# read the matches
numbers_matched_all = []
cards = []
for line in f:
    ix1 = line.index(':')
    ix2 = line.index('|')
    numbers_winning = re.findall(r'\d+', line[ix1+1:ix2-1])
    numbers_hand = re.findall(r'\d+', line[ix2:-1])
    numbers_matched = 0
    for number in numbers_winning:
        if number in numbers_hand:
            numbers_matched = numbers_matched + 1
    numbers_matched_all.append(numbers_matched)
    cards.append(1)

for num_card,num_matched in enumerate(numbers_matched_all):
    print('Card number', num_card, 'number matched',num_matched)
    for i in range(1,num_matched+1):
        cards[num_card+i] = cards[num_card+i] + cards[num_card]
    print('Total cards', cards[num_card])

print('Total cards', sum(cards))