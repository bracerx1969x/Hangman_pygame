from random import choice
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
WORD_CHOICES = ['python', 'java', 'kotlin', 'javascript']
MAX_TRIES = 8
DEBUG = False
WIN_GAME, LOSE_GAME, PLAYING = 'win', 'lose', 'playing'
PLAY, EXIT = 'play', 'exit'


class Hangman:
    def __init__(self, word_list, max_tries=MAX_TRIES):
        self.__secret_word = list(choice(word_list))
        self.revealed_word = list('-' * len(self.__secret_word))
        self.tries_left = max_tries
        self.guesses_list = set()
        self.game_status = PLAYING

    def show_revealed_word(self) -> str:
        return ''.join(self.revealed_word)

    def get_guess(self) -> str:
        print('\n' + game.show_revealed_word())
        this_guess = input('Input a letter: ')
        if DEBUG:
            print(f'guess = {this_guess}')
            print(f'previous guesses = {self.guesses_list}')

        # test guess correctness
        if len(this_guess) != 1:
            self.__wrong_guess('You should input a single letter', 0)
        elif this_guess not in ALPHABET:
            self.__wrong_guess('It is not an ASCII lowercase letter', 0)
        elif this_guess in self.guesses_list:
            self.__wrong_guess('You already typed this letter', 0)
        elif this_guess not in self.__secret_word:
            self.__wrong_guess('No such letter in the word', 1)
        else:  # good guess: passed all tests
            self.reveal_letters(this_guess)
        self.guesses_list.add(this_guess)

        return self.get_game_status()

    def get_game_status(self) -> str:
        if self.revealed_word == self.__secret_word:
            self.game_status = WIN_GAME
        if self.tries_left == 0:
            self.game_status = LOSE_GAME
        return self.game_status

    def __wrong_guess(self, message, penalty=1):
        self.tries_left -= penalty
        print(message)

    def reveal_letters(self, guessed_letter) -> str:
        for _index, each_letter in enumerate(self.__secret_word):
            if guessed_letter == each_letter:
                self.revealed_word[_index] = guessed_letter
        return self.show_revealed_word()


def displayMenu(show_title=True) -> str:
    # display title
    if show_title:
        print('H A N G M A N')
    action = input(f'Type "{PLAY}" to play the game, "{EXIT}" to quit: ')
    return action


play_game = displayMenu(show_title=True)

while play_game == 'play':
    game = Hangman(WORD_CHOICES, MAX_TRIES)
    playing = PLAYING
    while playing == PLAYING:
        playing = game.get_guess()
        if playing == WIN_GAME:
            print('You guessed the word!')
            print('You survived!')
        if playing == LOSE_GAME:
            print('You are hanged!')
    # ask to start a new game
    play_game = displayMenu(show_title=False)
    game = ''
