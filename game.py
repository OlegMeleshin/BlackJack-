from collections import OrderedDict
import random


class Deck:

    def __init__(self):
        self.deal = self.new_deck()

    def new_deck(self):
        """ Создает колоду в виде словаря {карта масти : ценность} """

        def suit_by_one(suit_name):
            """ Принимает название масти и 'раскрашивает' карты """

            names = ['Two', 'Three', 'Four', 'Five',
                     'Six', 'Seven', 'Eight', 'Nine',
                     'Ten', 'Jack', 'Queen', 'King',
                     'Ace']
            raw = []
            for card in names:
                raw.append(card + ' of ' + suit_name)

            card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

            suit = dict(zip(raw, card_value))

            return suit

        hearts = suit_by_one('Hearts')
        diamonds = suit_by_one('Diamonds')
        spades = suit_by_one('Spades')
        clubs = suit_by_one('Clubs')

        deck = {}
        """ Склеивает в одну колоду """
        deck.update(hearts)
        deck.update(diamonds)
        deck.update(spades)
        deck.update(clubs)

        """ Тасует колоду, возвращает словарь """
        deck = OrderedDict(deck)
        deck = list(deck.items())
        random.shuffle(deck)
        fin_deck = dict(deck)

        return fin_deck

    def pop_card(self):
        """ Достает по одной """
        next_card = self.deal.popitem()
        return next_card

    def cards_left(self):
        return len(self.deal)

class Gambler:

    def __init__(self):
        self.chips = 100
        self.hand = []
        self.score = 0

    def take_one_more(self, card):
        self.hand.append(card[0])

        if card[1] == 11: #проверка на туза
            if self.score + card[1] > 21:
                card = (card[0], 1)
        self.score += card[1]

    def new_hand(self):
        self.hand.clear()
        self.score = 0

class Dealer(Gambler):

    def __init__(self):
        self.chips = 1000
        self.hand = []
        self.score = 0





#####################################################





class Game():

    def __init__(self):
        self.deck = Deck()
        self.player = Gambler()
        self.dealer = Dealer()


    def print_dealer_hand(self):
        c = {"Dealer hand is ": None}
        a = []
        print(f"\nDealer hand is ", end='')
        for card in self.dealer.hand:
            print(card, end=', ')
            a.append(card)
            a.append(", ")
        print(f"{self.dealer.score} scores.")
        a.append(str(self.dealer.score))
        a.append(" scores.")
        b = "".join(a)
        c["Dealer hand is "] = b
        return c

    def return_first_card(self, card):
        c = {"Dealer hand is ": None}
        a = []
        a.append(card[0])
        a.append(", ")
        a.append(str(card[1]))
        a.append(" scores.")
        b = "".join(a)
        c["Dealer hand is "] = b
        return c

    def print_player_hand(self):
        c = {"Your hand is ": None}
        a = []
        print(f"\nYour hand is ", end='')
        for card in self.player.hand:
            print(card, end=', ')
            a.append(card)
            a.append(", ")
        print(f"{self.player.score} scores.")
        a.append(str(self.player.score))
        a.append(" scores.")
        b = "".join(a)
        c["Your hand is "] = b
        return c



    def check_blackjack(self, who):
        """Проверяет Блекджек"""
        if who.score == 21:
            return True
        else:
            return False

    def check_black_jack_win(self):
        """Победа блекджека с раздачи"""
        if self.check_blackjack(self.dealer) and self.check_blackjack(self.player):
            print("Draw")
            return "Draw"
        elif self.check_blackjack(self.dealer) and not self.check_blackjack(self.player):
            print("Dealer wins")
            return "Dealer wins"
        elif self.check_blackjack(self.player) and not self.check_blackjack(self.dealer):
            print(self.player.hand, "Player wins")
            return "Player wins"

    def check_black_jack_win_main(self):
        """Проверка на победу блекджека с раздачи"""
        if self.check_black_jack_win() == "Draw":
            self.print_dealer_hand()
            print(f"\Draw.")
            return True, "Draw", self.print_dealer_hand()

        if self.check_black_jack_win() == "Dealer wins":
            self.print_dealer_hand()
            print(f"\nYou loose.")
            return True, "You loose", self.print_dealer_hand()

        if self.check_black_jack_win() == "Player wins":
            self.print_dealer_hand()
            print(f"\nYou win!")
            return True, "You win", self.print_dealer_hand()

    def first_turn(self):
        """Игроки сбрасывают карты"""
        self.player.hand.clear()####
        self.dealer.hand.clear()####

        """Показывает одну"""
        self.first_card = self.deck.pop_card()
        self.dealer.take_one_more(self.first_card)
        self.print_dealer_hand()

        """Игрок набирает карты"""
        self.player.take_one_more(self.deck.pop_card())
        self.player.take_one_more(self.deck.pop_card())
        self.print_player_hand()


        """Диллер добирает карты"""
        self.dealer.take_one_more(self.deck.pop_card())
        end_round = self.check_black_jack_win_main()
        if end_round:
            return "End round"


    def player_lead(self):
        while True:
            lead = input(f"\nMake your lead:\n + to Hit\n - to Surrender\n = to Stand\n ++ for DoubleDown\n")

            if lead == "-":
                print(end='\r' + "Surrender")
                print(f"\nYou loose.")
                return "Surr"

            elif lead == "=":
                print(end='\r' + "Standing")
                return "Robot`s turn"

            elif lead == "++":
                print(end='\r' + "Doubledown")
                self.player.take_one_more(self.deck.pop_card())
                if self.player.score > 21:
                    print("\nBust! Dealer wins")
                    return "Player bust"
                return "Robot`s turn"

            elif lead == "+":
                self.player.take_one_more(self.deck.pop_card())
                self.print_player_hand()
                if self.player.score > 21:
                    print("\nBust! Dealer wins")
                    return "Player bust"

                while True:
                    lead = input(f"Make your lead:\n + to Hit\n = to Stand\n")
                    if lead == "+":
                        print(end='\r' + "Hit")
                        self.player.take_one_more(self.deck.pop_card())
                        self.print_player_hand()
                        if self.player.score > 21:
                            print("\nBust! Dealer wins")
                            return "Player bust"
                    elif lead == "=":
                        print(end='\r' + "Stand")
                        return "Robot`s turn"
                    else:
                        continue
            else:
                continue


    def robot_turn(self):
        while True:
            if self.dealer.score > 21:
                self.print_dealer_hand()
                print(f"\nBust! You win!")
                return "Robot bust"
            if self.dealer.score > 17:
                self.print_dealer_hand()
                return "Robot stand"
            else:
                self.dealer.take_one_more(self.deck.pop_card())


    def finalle(self):
        print(f"You have {self.player.score} points.\n Robot has {self.dealer.score} points")
        if self.dealer.score > self.player.score:
            print(f"\nYou loose.")
            return "You Loose"
        elif self.dealer.score == self.player.score:
            print(f"\nDraw.")
            return "Draw"
        elif self.player.score > self.dealer.score:
            print(f"\nYou win!")
            return "You Win"







