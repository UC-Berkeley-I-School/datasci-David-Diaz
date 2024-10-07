def score_word(word):
    """
    Calculate a score of the word based on the pre-defined Scrabble scoring rules

    Input:
    word (str): The word to score.

    Output:
    int: Score of the word.
    """
    scores =  {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    score = sum(scores.get(letter.lower(), 0) for letter in word)
    return score
