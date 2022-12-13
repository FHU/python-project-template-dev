import re  # you can use this module for a one line replacement of all punctuation


def nth_most_common_words(path, n):
    """The nth_most_common_words function takes the path to the script file and the
    word frequency rank and returns a list of words at that rank
    return an empty string if the rank is below 1 or if the rank does not exist"""
    words = get_words(path)
    word_counts = count_words(words)

    return


def count_words(word_list):
    """The count_words function takes a word list and returns a dictionary with
    the word as key and the value is the word count for that word"""
    pass


def get_words(path):
    """The get_words function takes a file path and returns a filtered list of
    the words in the file.
    The words should all be lowercase
    It filters out all the punctuation except contractions (they count as their own words)."""
    words = []
    for line in open(
        path
    ):  # loop through every line in the file. path should be a string
        pass  # of the file path to the script.


def word_probability(path, word):
    """The word probability function takes a file path and a word and returns a float
    that is a decimal value of the probability that any single word in the script
    would be that word.
    If the word is not in the script, the probability is 0"""
    words = get_words(path)
    word_counts = count_words(words)

    return


if __name__ == "__main__":
    # For extra practice, this would be a fun place to put a menu to access script stats
    # path = input("path: ")
    # n = int(input("n: "))
    # word = input("word: ")

    path = "test.txt"
    n = 3
    word = "the"

    words = nth_most_common_words(path, n)
    print(words)

    prob = word_probability(path, word)
    print(prob)
