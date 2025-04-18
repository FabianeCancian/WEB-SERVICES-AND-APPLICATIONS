import requests
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
deck = response.json()

url = f"https://deckofcardsapi.com/api/deck/{deck['deck_id']}/draw/?count=5"
response = requests.get(url)
deck = response.json()
cards = deck['cards']

# A (for an ace), 2, 3, 4, 5, 6, 7, 8, 9, 0 (for a ten), J (jack), Q (queen), or K (king);
# S (Spades), D (Diamonds), C (Clubs), or H (Hearts).
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0','J','Q','K']

def pokerTime(cards):
    # vars for Flush
    spades = 0
    diamonds = 0
    clubs = 0
    hearts = 0

    # var for straight
    straight = []

    for card in cards:
        if (card['suit'] == 'SPADES'):
            spades = spades + 1
        if (card['suit'] == 'DIAMONDS'):
            diamonds = diamonds + 1
        if (card['suit'] == 'CLUBS'):
            clubs = clubs + 1
        if (card['suit'] == 'HEARTS'):
            hearts = hearts + 1

        straight.append(card['code'][0])

    if(spades == 5 or diamonds == 5 or clubs == 5 or hearts == 5):
        print('Congratulations you made a flush')
    
    print(', '.join(map(str, values)) in ', '.join(map(str, straight)))

for card in cards:
    print (card['value'])
    print (card['suit'])

pokerTime(cards)



