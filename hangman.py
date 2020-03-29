from random import randint

class Player():
    def __init__(self, name='Player'):
        self.name = name


class Game():
    def __init__(self, word, name='Player'):
        self.player = Player(name)
        self.word = list(word)
        self.guesses_left = len(word)
        self.guessed_letters = set()

    def start_game(self):
        hidden_word = ['-' for x in range(len(self.word))]

        print('Hello {}, would you like to play Hangman?'.format(self.player.name))
        play_again = True if input('Y/N: ').lower() == 'y' else False
        self.guesses_left = int(input('Input how many guesses you want: '))

        while play_again:
            print()
            print(''.join(hidden_word))
            guess = input(': ')

            if guess in self.guessed_letters:
                print('You have already guessed that letter!')
                self.guesses_left -= 1
            elif guess in self.word:
                print('Correct')
                self.guessed_letters.add(guess)
                for idx, letter in enumerate(self.word):
                    if guess == letter:
                        hidden_word[idx] = letter
            elif list(guess) == self.word:
                print('Wow, the whole word in one guess!')
                hidden_word = self.word
            else:
                print('Wrong, that letter is not in the word!')
                self.guesses_left -= 1
                self.guessed_letters.add(guess)
                    
            if self.check_win(hidden_word) or self.check_lost():
                print('Would you like to play again?')
                play_again = True if input('Y/N: ').lower() == 'y' else False
                if play_again:
                    self.guesses_left = int(input('Input how many guesses you want: '))
                    hidden_word = ['-' for x in range(len(self.word))]

            else:
                print('Number of guesses left: {}'.format(self.guesses_left))
                print('Guessed characters: {}'.format(', '.join(sorted(self.guessed_letters))))

        return False

            
    def check_lost(self):
        if self.guesses_left == 0:
            print('You Lost. :(')
            print('The word was:',''.join(self.word))
            return True
        return False

    def check_win(self, hidden_word):
        if hidden_word == self.word:
            print('You Won! :)')
            print('The word was:',''.join(self.word))
            return True
        return False
        

def get_word(filename):
    words_list = []
    with open(filename, "r") as f:
        for word in f:
            words_list.append(word.strip())
    return words_list[randint(0, len(words_list) - 1)]

def run_game():
    word = get_word("/Users/bjartur/Desktop/HR/2_onn/T-201-GSKI/Project Assignments/06/words.txt")
    game = Game(word)
    
    game.start_game()

run_game()
