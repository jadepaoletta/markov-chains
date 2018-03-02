"""Generate Markov text from text files."""

from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path, "r")
    file_string = file.read()
    file.close()
    return file_string


def make_chains(text_string):
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

    for count in range(len(text_list) - 2):
        
        key_bigram = (text_list[count], text_list[count+1])
        chains[key_bigram] = chains.get(key_bigram, [])
        chains[key_bigram].append(text_list[count+2])

    print chains


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    first_tuple = choice(chains.keys())
    words.extend([first_tuple[0], first_tuple[1]])

    while first_tuple in chains:
        next_word = choice(chains[first_tuple])
        words.append(next_word)
        first_tuple = (first_tuple[1], next_word)

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
