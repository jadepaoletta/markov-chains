"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path, "r")
    file_string = file.read()
    file.close()
    return file_string


def make_chains(text_string, n_grams):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text_list = text_string.split()

    for count in range(len(text_list) - n_grams):
        key_ngram = []
        counter = count

        while counter < count + n_grams:
            key_ngram.append(text_list[counter])
            counter += 1

        key_bigram = tuple(key_ngram)

        chains[key_bigram] = chains.get(key_bigram, [])
        chains[key_bigram].append(text_list[count+n_grams])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    chains_upper = [key for key in chains.keys() if key[0][0].isupper()]
    first_tuple = choice(chains_upper)
    words.extend(list(first_tuple))

    while first_tuple in chains:
        next_word = choice(chains[first_tuple])
        words.append(next_word)
        next_tuple_list = list(first_tuple[1:])
        next_tuple_list.append(next_word)
        first_tuple = tuple(next_tuple_list)

    punct = ['?', '.', ',', '--']

    for count, word in reversed(list(enumerate(words))):
        if word[-1] not in punct:
            del words[count]
        else:
            break

    return " ".join(words)


input_path = sys.argv[1]
n_grams = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_grams)

# Produce random text
random_text = make_text(chains)

print random_text
