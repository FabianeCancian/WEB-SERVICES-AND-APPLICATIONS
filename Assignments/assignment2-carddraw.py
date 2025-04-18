import requests
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
deck = response.json()

url = f"https://deckofcardsapi.com/api/deck/{deck['deck_id']}/draw/?count=5"
response = requests.get(url)
deck = response.json()
cards = deck['cards']

for card in cards:
    print (f"Card: {card['value']} of {card['suit']}")

## Last few marks

# A (for an ace), 2, 3, 4, 5, 6, 7, 8, 9, 0 (for a ten), J (jack), Q (queen), or K (king);
# S (Spades), D (Diamonds), C (Clubs), or H (Hearts).
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13]

def check_flush(cards):
    spades = 0
    diamonds = 0
    clubs = 0
    hearts = 0

    for card in cards:
        if (card['suit'] == 'SPADES'):
            spades = spades + 1
        if (card['suit'] == 'DIAMONDS'):
            diamonds = diamonds + 1
        if (card['suit'] == 'CLUBS'):
            clubs = clubs + 1
        if (card['suit'] == 'HEARTS'):
            hearts = hearts + 1

    if(spades == 5 or diamonds == 5 or clubs == 5 or hearts == 5):
        print('Congratulations you made a flush')

def check_straight(cards):
    straight = []

    for card in cards:
        card_short_code_value = card['code'][0]

        if(card_short_code_value == 'A'):
            card_short_code_value = '1'
        if(card_short_code_value == '0'):
            card_short_code_value = '10'
        if(card_short_code_value == 'J'):
            card_short_code_value = '11'
        if(card_short_code_value == 'Q'):
            card_short_code_value = '12'
        if(card_short_code_value == 'K'):
            card_short_code_value = '13'

        straight.append(int(card_short_code_value))

    straight.sort()
    is_straight = ', '.join(map(str, straight)) in ', '.join(map(str, values))
    #https://www.geeksforgeeks.org/python-check-if-a-list-is-contained-in-another-list/

    if (is_straight):
        print('Congratulations you got a straight')

def check_pair_triple(cards):
    card_value_list = []
    for card in cards:
        card_value_list.append(card['value'])

    no_duplicates = list(dict.fromkeys(card_value_list))
    #https://www.w3schools.com/python/python_howto_remove_duplicates.asp
    for card in no_duplicates:
        count = card_value_list.count(card)
        #https://www.w3schools.com/python/ref_list_count.asp
        if (count == 3):
            print(f'you got a triple of {card}')
        if (count == 2):
            print(f'you got a pair of {card}')

check_flush(cards)
check_straight(cards)
check_pair_triple(cards)

