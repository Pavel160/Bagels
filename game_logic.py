import random
from config import NUM_DIGITS


def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:NUM_DIGITS])


def getClues(guess, secretNum):
    """Возвращает строку с подсказками "Pico", "Fermi" и "Bagels"."""
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if not clues:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)
