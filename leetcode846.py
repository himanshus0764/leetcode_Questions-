hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3

if len(hand) % groupSize != 0:
    print(False)
    
card_count = {}
for card in hand:
    card_count[card] = card_count.get(card, 0) + 1

while card_count:
    min_card = min(card_count)
    for i in range(min_card, min_card + groupSize):
        if i not in card_count:
            print(False)
        card_count[i] -= 1
        if card_count[i] == 0:
            del card_count[i]

print(True)
