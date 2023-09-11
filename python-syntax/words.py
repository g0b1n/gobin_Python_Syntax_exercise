
def print_upper_words(words):

    """
    Print each words on seperate lines. They all should be UPPERCASED.
    For example:
    print_upper_words(["apple", "orange", 'mango])
    APPLE
    ORANGE
    MANGO
    """

    for word in words:
        print(word.upper())

def print_upper_words_E(words):
    """
    print UPPERCASED words on seperate lines if they start with E/e
    """

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())

def print_upper_word_3(words, must_start_with):
    """
    print each word on sepereate lines if they are UPPERCASED and starts with any given letters
    """

    for word in words:
        for letter in must_start_with:
            print(word.upper())
            break