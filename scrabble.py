from wordscore import score_word

def run_scrabble(letters):
    """
    Run the Scrabble game using the provided letters

    Input: 
    Letters(str): String of letters

    Returns:
    tuple: A list of valid Scrabble words with their scores
    
    """
    letters = letters.upper()
    
    # Check for input errors
    if len(letters) < 2 or len(letters) > 7:
        return "Error: Input must be between 2 and 7 characters."
    
    if not all(c.isalpha() or c in '*?' for c in letters):
        return "Error: Input can only contain letters (A-Z) and wildcards (* or ?)."
    
    if letters.count('*') > 1 or letters.count('?') > 1:
        return "Error: Only one wildcard of each type (* and ?) is allowed."
    
    # Replace wildcards with empty strings for processing
    wildcards = [letters.count('*'), letters.count('?')]
    letters = letters.replace('*', '').replace('?', '')

    valid_words = []

    # Load the dictionary of valid words
    with open("sowpods.txt", "r") as infile:
        raw_input = infile.readlines()
        example_dictionary = [datum.strip('\n') for datum in raw_input]

    # Check for words that can be formed
    for word in example_dictionary:
        if can_form_word(word, letters, wildcards):
            score = score_word(word)
            valid_words.append((score, word.upper()))
    
    # Sort words by score and then alphabetically
    valid_words.sort(key=lambda x: (-x[0], x[1]))

    # Return the results
    return valid_words, len(valid_words)


def can_form_word(word, letters, wildcards):
    """
    Checks to see if the letters form a word.

    Input:
    word (str): the word to check
    letters (str): the available letters
    wildcards (list): LIst containing the counts of '*' and '?' wildcards

    Returns:
    Boolean: True or False
    """
    # Count the letters in the available letters
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    # Check each letter in the word
    for letter in word:
        if letter in letter_count and letter_count[letter] > 0:
            letter_count[letter] -= 1
        elif wildcards[0] > 0:
            wildcards[0] -= 1 
        elif wildcards[1] > 0: 
            wildcards[1] -= 1 
        else:
            return False
    return True 
