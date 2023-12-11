import re
f = open('input.txt')

sum_tickets = 0
for line in f:
    ix1 = line.index(':')
    ix2 = line.index('|')
    numbers_winning = re.findall(r'\d+', line[ix1+1:ix2-1])
    numbers_hand = re.findall(r'\d+', line[ix2:-1])
    card_value = 0
    numbers_matched = []
    for number in numbers_winning:
        if number in numbers_hand and card_value == 0:
            card_value = card_value + 1
            numbers_matched.append(number)
        elif number in numbers_hand and card_value > 0:
            card_value = 2*card_value
            numbers_matched.append(number)

    print(line[0:-1])
    print(numbers_matched, card_value)
    sum_tickets = sum_tickets + card_value

print('Sum of all tickets', sum_tickets)