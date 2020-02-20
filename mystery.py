import random
# WORDLIST = 'words.txt'

class Game:
    def __init__(self):
        self.player = Player("Player")


    def get_random_word(min_word_length):
        """ Getting random word from list."""
        pass
       


class Player:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'{self.name}'


Game()