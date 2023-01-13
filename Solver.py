
class WordleSolver:
    def __init__(self, words, letters_frequency):
        self.words = words
        self.letters_frequency = letters_frequency
        self.order_words_by_frequency()
        self.guess = ''

    def order_words_by_frequency(self):
        return list(sorted(self.words, key=self.rank_word, reverse=True))

    def rank_word(self, word):
        return sum(set([self.letters_frequency[letter] for letter in word]))

    def computer_guess(self, result):
        if result:
            self.filter_words(result)
        self.guess = self.words[0]
        return self.words[0]

    def filter_words(self, result):
        legal, perfect, wrong = self.letters_information(result, self.guess)

        def filter_by_wrong_perfect_legal_letters(word):
            # check if two lists intersect
            contain_wrong_letters = list(set(wrong) & set(list(word)))

            contain_perfect_letters = True
            for l, i, in perfect.items():
                if l != word[i]:
                    contain_perfect_letters = False
                    break

            contain_legal_letters = True
            for l in legal:
                if l not in word:
                    contain_legal_letters = False
                    break
            return (not contain_wrong_letters) and contain_perfect_letters and contain_legal_letters

        self.words = list(filter(filter_by_wrong_perfect_legal_letters,self.words))

    def letters_information(self, guess_information, word):
        legal = []
        wrong = []
        perfect = {}
        for i in range(len(guess_information)):
            if guess_information[i] == 0:
                wrong.append(word[i])
            if guess_information[i] == 1:
                legal.append(word[i])
            if guess_information[i] == 2:
                perfect[word[i]] = i
        return legal, perfect, wrong








