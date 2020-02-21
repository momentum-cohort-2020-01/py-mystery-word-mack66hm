import random

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.word_letters = []
        self.blank_list = []


    def play_game(self):
        with open('words.txt', 'r') as file:
            data = file.read()
        print("Welcome to Mystery Word Game, a game where you try to guess the correct word.")
        print("There are 3 different levels: " " (E)asy gives you a word between 4-6 letters." " (M)edium gives you a word between 7-8 letters." " (H)ard gives you a word with 8 or more letters.")
        diff = input("Which level do you want to play: ")
        diff = diff.lower()
        if diff == 'e':
            word_list = [word for word in data.split() if len(word) >3 and len(word) < 7]
        elif diff == 'm':
            word_list = [word for word in data.split() if len(word) >6 and len(word) < 9]
        elif diff == 'h':
            word_list = [word for word in data.split() if len(word) > 8]
        else:
            print("Please pick which level.")
            Game().play_game()
        print('Guess one letter at a time until the whole word is shown. You have 8 wrong guesses!')
        word = random.choice(word_list)
        word = word.lower()
        print(word)
        word_length = len(word)
        word_letters = list(word)
        blank_list = ['_'] * word_length
        guessing_list = []
        print(" ".join(blank_list))
        print("Your word has " f'{word_length}' " letters!")
        while "_" in blank_list:
            playing = True
            while playing:
                choice = input("What is your guess: ")
                choice.lower()
                if choice.isalpha() and len(choice) == 1:
                    if choice in guessing_list:
                        print("You already have guessed this letter try again")
                    elif choice in word_letters:
                        index_position_list = self.find_index_positions(word_letters, choice)
                        choice_list = len(index_position_list) * [choice,]
                        for (index, choice) in zip(index_position_list, choice_list):
                            blank_list[index] = choice
                        print(" ".join(blank_list))
                        print("You are correct!!!")
                        guessing_list.append(choice)
                    else:
                        self.player.number_of_turns_left -= 1
                        print("That is not correct. You have " f'{self.player.number_of_turns_left}' " turns left"" ")
                        guessing_list.append(choice)
                else:
                    print("You can enter letters from A-Z, and only one letter at a time.")
                if self.player.number_of_turns_left == 0:
                    self.start_new_game(word)
                    break
            playing = False
            self.start_new_won(word)

    
    # def find_index_positions(self, word_letters, choice):
    #     index_position_list = []
    #     index_position = 0
    #     while True:
    #         try:
    #             index_position = word_letters.index(choice, index_position)
    #             index_position_list.append(index_pos)
    #             index_position += 1
    #         except:
    #             break
    #     return index_position_list  


    # def list_to_string(self, blank_list):
    #     str = " "
    #     return (str.join(blank_list))

    
    def start_new_game(self, word):
        print("You have no more guesses left. The correct word was: " f'{word}')
        play_new_game = input("Press S to (S)tart Or press anyting else to leave. ")
        play_new_game = play_new_game.lower()
        if play_new_game == "r":
            Game().play_game()
        else:
            print("See you next time bye!")
            exit()
    

    def start_new_won(self, word):
        print("Congratulations, you won! You guessed " f'{word}' "correct! ")
        play_new_game = input("Press S to (S)tart Or press anyting else to leave. ")
        play_new_game = play_new_game.lower()
        if play_new_game == "r":
            Game().play_game()
        else:
            exit()


    def find_index_positions(self, word_letters, choice):
        index_position_list = []
        index_position = 0
        while True:
            try:
                index_position = word_letters.index(choice, index_position)
                index_position_list.append(index_position)
                index_position += 1
            except:
                break
        return index_position_list  
    



class Player:
    def __init__(self, name):
        self.name = name
        self.number_of_turns_left = 8
        


game = Game()
Game().play_game()




# for i in range(len(game_word)):
#             if game_word[i] in game_word_letters:
#                 underscore_list = underscore_list[:i] + game_word[i] + game_word[i+1:]