import random

class PokerGame:
    def __init__(self):
        self.players = {}
        self.pot = 0

    def add_player(self, player_name):
        self.players[player_name] = {'cards': [], 'bet': 0}
        print(f"Server: {player_name} has joined the game.")

    def deal_cards(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
        random.shuffle(deck)

        for player in self.players:
            self.players[player]['cards'] = [deck.pop(), deck.pop()]
            print(f"Server: {player}'s cards: {', '.join(self.players[player]['cards'])}")

    def place_bet(self, player_name, bet_amount):
        if player_name in self.players:
            self.players[player_name]['bet'] += bet_amount
            self.pot += bet_amount
            print(f"Server: {player_name} has bet {bet_amount}. Total pot: {self.pot}")

    def show_pot(self):
        print(f"Server: Total pot is now {self.pot}")

# สร้างเกมโป๊กเกอร์
poker_game = PokerGame()

# เพิ่มผู้เล่น
poker_game.add_player("Player1")
poker_game.add_player("Player2")

# แจกไพ่
poker_game.deal_cards()

# ตัวอย่างการเดิมพัน
poker_game.place_bet("Player1", 50)
poker_game.place_bet("Player2", 75)

# แสดงยอดเงินในหม้อ
poker_game.show_pot()
