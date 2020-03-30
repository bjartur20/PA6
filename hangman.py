from random import randint

class Player():
    def __init__(self, name='Player'):
        self.name = name


class Game():
    def __init__(self, name='Player'):
        self.player = Player(name)
        self.guessed_letters = set()
        self.wins = 0
        self.losses = 0

    def start_game(self):
        select = self._display_menu()
        if select == 1:
            self._hang_man(select)
        elif select == 5:
            return

    def _hang_man(self, select):
        word = list(get_word('words.txt'))
        hidden_word = self._get_hidden_word(word)
        guesses_left = int(input('Input how many guesses you want: '))
        while select == 1:
            print()
            print(''.join(hidden_word))
            guess = input(': ')

            if guess in self.guessed_letters:
                print('You have already guessed that letter!')
                guesses_left -= 1
            elif guess in word:
                print('Correct')
                self.guessed_letters.add(guess)
                for idx, letter in enumerate(word):
                    if guess == letter:
                        hidden_word[idx] = letter
            elif list(guess) == word:
                print('Wow, the whole word in one guess!')
                hidden_word = word
            else:
                print('Wrong, that letter is not in the word!')
                guesses_left -= 1
                self.guessed_letters.add(guess)
                    
            if self._check_win(word, hidden_word) or self._check_lost(word, guesses_left):
                print('----------------')
                print('1. Play again')
                print('2. Menu')
                print('----------------')
                select = int(input(': '))
                if select == 1:
                    self._hang_man(select)
                elif select == 2:
                    self.start_game()
                    return
            else:
                print('Number of guesses left: {}'.format(guesses_left))
                print('Guessed characters: {}'.format(', '.join(sorted(self.guessed_letters))))
    
    def _check_lost(self, word, guesses_left):
        if guesses_left == 0:
            print('You Lost. :(')
            print('The word was:',''.join(word))
            self.losses += 1
            return True
        return False

    def _check_win(self, word, hidden_word):
        if hidden_word == word:
            print('You Won! :)')
            print('The word was:',''.join(word))
            self.wins += 1
            return True
        return False

    def _display_menu(self):
        while True:
            print('----------------')
            print('1. Play Hangman')
            print('2. Add words to wordbank')
            print('3. View highscores')
            print('4. View game history')
            print('5. Quit')
            print('----------------')
            
            select = int(input(': '))

            return select

    def _get_hidden_word(self, word):
        return ['-' for x in range(len(word))]
        

def get_word(filename):
    words_list = []
    with open(filename, "r") as f:
        for word in f:
            words_list.append(word.strip())
    return words_list[randint(0, len(words_list) - 1)]

def run_game():
    game = Game()
    game.start_game()

run_game()
