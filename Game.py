import random

"""Game object - the game is in charge of managing and running the game in user or computer mode """


class Game:
    def __init__(self, words, guesses, solver, word_length=5):
        """
        initializing the Game Object
        :param words: all words in English with length of word_length input
        :param guesses: amount of guesses you give to the user/computer
        :param solver: solver object - in charge of solving the computer algorithm
        :param word_length: decide word length for the game
        """
        self.words = words
        self.guesses = guesses
        self.solution = self.choose_random_word(word_length)
        self.solver = solver

    def choose_random_word(self, word_length):
        """
        computer guess
        :param word_length: word length
        :return: computer guess
        """
        chosen_word = random.choice(self.words)
        while word_length != len(chosen_word):
            chosen_word = random.choice(self.words)
        return chosen_word

    def analayze_guess(self, guess):
        """
        :param guess: string that represent the last guess
        :return: inteher list - information about last guess
        """
        if guess == self.solution:
            return [2] * len(guess)
        information = [0] * len(guess)
        for i in range(len(guess)):
            if guess[i] == self.solution[i]:
                information[i] = 2
            elif guess[i] in self.solution:
                information[i] = 1
        return information

    def get_user_guess(self, word_length):
        """
        :param word_length: to check guess length
        :return: user's guess
        """
        user_guess = input('Hi! Please guess a word:')
        while len(user_guess) != word_length or user_guess not in self.words:
            print('Error: word is not legal, Please try again')
            user_guess = input('guess a word:')
        return user_guess

    def run_game(self, game_mode):
        """
        function that runs the game
        :param game_mode: user/copmuter
        :return: guess remains in the and of the game
        """
        result = []
        while self.guesses > 0:
            guess = self.get_user_guess(5) \
                if game_mode == 'user' else self.solver.computer_guess(result)
            print(guess)
            result = self.analayze_guess(guess)
            if result == [2] * len(guess):
                print('You won!!')
                return self.guesses
            else:
                print(result)
                self.guesses -= 1
                print('Wrong guess! you have ' + str(self.guesses) + ' guesses left')
        print('You are out of guesses... you stupid fuck! Game over.')
        return self.guesses
