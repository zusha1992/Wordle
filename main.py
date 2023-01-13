from Game import Game
from Solver import WordleSolver

"""
main file - run and get average results
"""

words = 'video quest river choke tiger shine grave rough ' \
        'floor honor speed chief agree cause think issue essay ' \
        'force shoot anger proud tasty first taste organ amber ankle ' \
        'catch grace chaos stuff quota swear forum feast ample shame blade ' \
        'frank sight arena cater clash outer ivory train wrist right spray slime ' \
        'yearn leave handy point nerve sword stuff hover video grind world index ' \
        'thigh solve tribe funny ghost proud ivory cabin sense spite mouth swear slant ' \
        'urine color split river enter worry frown novel lodge essay snack arise dirty braid ' \
        'floor wreck judge stain fairy fence error staff ferry'.split(
    ' ')

letters_frequency = {'a': 0.08167, 'n': 0.06749,
                     'b': 0.01492, 'o': 0.07507,
                     'c': 0.02782, 'p': 0.01929,
                     'd': 0.04253, 'q': 0.00095,
                     'e': 0.12702, 'r': 0.05987,
                     'f': 0.02228, 's': 0.06327,
                     'g': 0.02015, 't': 0.09056,
                     'h': 0.06094, 'u': 0.02758,
                     'i': 0.06966, 'v': 0.00978,
                     'j': 0.00153, 'w': 0.02360,
                     'k': 0.00772, 'x': 0.00150,
                     'l': 0.04025, 'y': 0.01974,
                     'm': 0.02406, 'z': 0.00074}


def collect_average_score(repetitions):
    """
    :param repetitions: amount of play rounds
    :return: average result of guesses
    """
    guesses = 0
    for i in range(repetitions):
        game = Game(words, 5, WordleSolver(words.copy(), letters_frequency))
        guesses += game.run_game('computer')
    return 5 - (guesses / repetitions)


print(collect_average_score(100))
