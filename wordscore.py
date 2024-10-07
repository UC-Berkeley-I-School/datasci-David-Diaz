def score_word(word):
    """
    Calculate a score of the word based on the pre-defined Scrabble scoring rules

    Input:
    word (str): The word to score.

    Output:
    int: Score of the word.
    """
    score = 0
    SCRABBLE_SCORES =  {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    for letter in word.upper():  # Convert to uppercase for consistency
        score += SCRABBLE_SCORES.get(letter, 0)  # Add score or 0 if letter is not in the dictionary
    return score
