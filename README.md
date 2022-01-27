**Bee Movie script analysis**

Have you ever stopped to wonder, "How many times does is the word 'bee' spoken
in Bee Movie?" or "What is the 50th most common word in the movie?"

If you have, you're in luck! We get to write four functions to analyze the
words in the Bee Movie script.

```
nth_most_common_words(path, n)
    The nth_most_common_words function takes the path to the script file and the 
    word frequency rank and returns a list of words at that rank
    return an empty string if the rank is below 1 or if the rank does not exist

count_words(word_list)
    The count_words function takes a word list and returns a dictionary with
    the word as key and the value is the word count for that word

get_words(path)
    The get_words function takes a file path and returns a filtered list of
    the words in the file. 
    The words should all be lowercase
    It filters out all the punctuation except contractions (they count as their own words).

word_probability(path, word)
    The word probability function takes a file path and a word and returns a float
    that is a decimal value of the probability that any single word in the script
    would be that word.
    - If the word is not in the script, the probability is 0
```