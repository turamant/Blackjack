import random
from datetime import datetime

ruls = """В блэкджеке игроку и казино сдаются две карты из колоды. Цель
— набрать очки, но не превысить 21 очко. Стоимость карты равна
числу на ее лицевой стороне или 10, если карта — валет, дама или король, или 11, если карта — туз.
Если в руке два или более туза, то из общего количества очков в руке вычитается 10.
Игрок ходит первым и при желании получает дополнительные карты, говоря «еще карту». 
Когда счет игрока приближается к 21, игрок останавливается. Если после «еще карту» счет игрока
превышает 21, игра заканчивается победителем. Если нет, то настала
очередь Казино. Здесь мы упрощаем ситуацию, предполагая, что Казино запросит «ещё карту»,
если его общий балл меньше 17. После того, как Казино закончит игру, победителем становится тот,
кто наберет наибольшее количество очков, если этот балл меньше или равно 21. Возможны ничьи. """

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ['\u2660', '\u2661', '\u2662', '\u2663']


class Card:
    """ Card """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Hand:
    """ Hand """
    def __init__(self):
        self.hand_cards = list()

    def value(self):
        score = 0
        number_aces = 0
        for i in range(0, len(self.hand_cards)):
            if self.hand_cards[i].rank != "Ace" and self.hand_cards[i].rank != "King" and \
                    self.hand_cards[i].rank != "Queen" and self.hand_cards[i].rank != "Jack":
                int_val = int(self.hand_cards[i].rank)
                score += int_val
            elif self.hand_cards[i].rank == "Jack" or self.hand_cards[i].rank == "Queen" or \
                    self.hand_cards[i].rank == "King":
                score += 10
            elif self.hand_cards[i].rank == "Ace":
                score += 11
                number_aces += 1
        if score > 21 and number_aces > 1:
            score -= 10 * number_aces
        return score

    def add_card(self, card: Card):
        self.hand_cards.append(card)

    def display(self):
        print(*[x.rank + x.suit + ", " for x in self.hand_cards])



class Deck:
    """ Deck """
    def __init__(self):
        self.deck_cards = list()
        for suit in suits:
            for rank in ranks:
                self.deck_cards.append(Card(rank, suit))
        self.shuffle()

    def deal_card(self):
        top_card = self.deck_cards[0]
        self.deck_cards = self.deck_cards[1:]
        return top_card

    def shuffle(self):
        random.seed(datetime.now())
        random.shuffle(self.deck_cards)

    def display(self):
        for card in self.deck_cards:
            print(card.rank + ": " + card.suit)


if __name__ == '__main__':
    print("===================================== Правила игры Блек-Джек ======================================")
    print(ruls)
    while True:
        print("===================================== Новая игра ===============================================")
        print(f"Будете играть ?")
        result = input("Введите y/n: ")
        if result != "y":
            print("Good bye!")
            print("- - - - - - - - - - - - - - - - - - - Game Over - - - - - - - - - - - - - - - - - - - - -")
            break

        print("--------------------- Игра начата: --------------------")
        gameOver = False
        my_deck = Deck()

        house_hand = Hand()
        player_hand = Hand()

        for i in range(1, 3):
            card_house = my_deck.deal_card()
            house_hand.add_card(card_house)
            card_player = my_deck.deal_card()
            player_hand.add_card(card_player)

        # Основной интерактив игры

        print("Ваши карты: ")
        player_hand.display()
        print("------------------------------------")
        print(f"У вас {player_hand.value()} очков . Хотите еще карту ? (y/n)")
        result = input("Введите y/n: ")
        while True:
            if result != "y":
                break
            card = my_deck.deal_card()
            player_hand.add_card(card)
            player_hand.display()
            if player_hand.value() > 21:
                print(f"Очки игрока: {player_hand.value()} превышают 21. Игра окончена. Казино победило!")
                print("У казино было: ", end="")
                house_hand.display()
                gameOver = True
                break
            print(f"У вас {player_hand.value()} ,Хотите еще карту ?")
            result = input("Введите y/n: ")
        if gameOver != True:
            while True:
                if house_hand.value() > 21:
                    print(f"у Казино: {house_hand.value()} очков. Перебор больше 21 очка. Игрок выиграл!{player_hand.value()} Game over!")
                    print("У казино было: ", end="")
                    house_hand.display()
                    gameOver = True
                    break
                if house_hand.value() < 17:
                    card = my_deck.deal_card()
                    house_hand.add_card(card)
                else:
                    break
        if gameOver != True:
            if player_hand.value() > house_hand.value():
                print(f"Счет игрока: {player_hand.value()} превышает счет казино:{house_hand.value()}.Game over. Player win!")
                print("У казино было: ", end="")
                house_hand.display()
            elif player_hand.value() == house_hand.value():
                print(f"Счет игрока: {player_hand.value()} равен счету казино:{house_hand.value()}. Game over! Ничья!")
                print("У казино было: ", end="")
                house_hand.display()

            else:
                print(f"«Счет Казино: {house_hand.value()} превышает счет игрока:{player_hand.value()}. Game оver!. Kasino win!")
                print("У казино было: ", end="")
                house_hand.display()

        print("- - - - - - - - - - - - - - - - - - - Game Over - - - - - - - - - - - - - - - - - - - - -")
        print()
        print()