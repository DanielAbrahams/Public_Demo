import random

class cardGame:

    #initiate class cardGame
    def __init__(self):
        self.message = 'An object is created'
        self.deck = []

        #buildDeck and the shuffleCards once cardGame class starts
        self.buildDeck()
        self.shuffleCards()


    #buld cardGame deck function
    def buildDeck(self):

        #instantiate highcard and suit value
        Jack = 11
        Queen = 12
        King = 13
        Ace = 14
        Spade = 1
        Diamond = 2
        Hearts = 3
        Clubs = 4

        #create low cards
        for suit in [Spade, Clubs, Diamond, Hearts]:
            for value in range (2,11):
                dict = [suit , value]
                self.deck.append(dict)

        #create high cards
        for suit in [Spade, Clubs, Diamond, Hearts]:
            for highcard in [Ace, King, Queen, Jack]:
                dict = [suit , highcard]
                self.deck.append(dict)

        return self.deck

    '''Randomly mix cards in the deck
        Return the whole deck of cards with a mixed order'''
    def shuffleCards(self):

        try:
            #use random to shuffle deck
            random.shuffle(self.deck)
            return self.deck

        except Exception as e:
            print(e)

    #returnCard function
    '''get a card from the top of deck
    return card
    if no card left return '''
    def returnCard(self):

        #test to see if cards are left if so return card

        if len(self.deck) != 0:
            returnCard = self.deck.pop(0)
            return returnCard
        elif len(self.deck) == 0:
            print("No Cards Left In Deck")
            raise Exception("No Cards Left In Deck")


    #emptyDeck function
    def emptyDeck(self):

        try:
            self.deck.clear()

        except Exception as e:
            print(e)

        return self.deck

    '''sort cards in ascending order but suit and rank'''
    def sortDeck(self):

        #use sort and lamdda function to sort deck
        self.deck.sort(key=lambda x: (x[0], x[1]))

        return self.deck

    '''determine winner of 2 players game
        they will draw 3 cards by taking turns'''
    def play(self):

        '''card value determined in buildDeck function'''

        #since 2 player are hard coded in question, players instantiated with list
        player1 = []
        player2 = []

        #return 3 cards for each player taking turns
        for i in range(3):
            card_a =  self.returnCard()
            self.shuffleCards()
            player1.append(card_a)
            card_b = self.returnCard()
            player2.append(card_b)


        player1_total_score = 0
        player2_total_score = 0

        #determined player1 score
        for i, k in player1:
            player1_card_score = (i * k)
            player1_total_score += player1_card_score

        player1 = player1_total_score

        #determined player2 score
        for i, k in player2:
            player2_card_score = (i * k)
            player2_total_score += player2_card_score

        player2 = player2_total_score

        #determine game winner
        if (player1 > player2):
            print("Player 1 is the winner")
            return player1
        elif (player1 < player2):
            print("Player 2 is the winner")
            return player2
        else:
            print("Game ended in a tie")


cardGame = cardGame()
cardGame.play()


