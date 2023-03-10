"""Generate Markov text from text files."""

from random import choice, randint

import sys

input_path = sys.argv[1]

def open_and_read_file(file_path=input_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open file
    with open(file_path) as file:

        # add everything in file to text as one string
        text = file.read()

    # return string of all the text
    return text

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    n = int(input('How many words do you want in your n-gram? Use an integer: '))

    # create list of words, splitting text string at each whitespace
    words = text_string.split()

    # create empty dictionary
    chains = {}

    # iterate over index values
    for i in range(len(words) - n):

        # define n number of items in tuple
        tuple_list = []
        for j in range(n):
            nth_word = words[i + j]
            tuple_list.append(nth_word)

        ngram = tuple(tuple_list)
        list_word = words[i + n] 

        # create tuple: next word dict entry. initialize list if tuple is new, add list word to list.
        chains[ngram] = chains.get(ngram, []) + [list_word]
    
    print(chains)
    # return the chains dictionary
    return chains


def make_text(chains):
    """Return text from chains."""

    # initialize blank words list
    words = []

    # Get first tuple
    # for key in chains:
    #     ngram = key
    #     words.extend(list(ngram))
    #     break

    # Get random first tuple starting with a capital letter 
    while True: 

        # use choice to get random tuple from chains
        ngram = choice(list(chains))

        # check if first letter of first word in tuple is uppercase
        if ngram[0][0].isupper():

            # add tuple to the words list
            words.extend(list(ngram))

            # leave the while loop
            break
    
    while True:
        
        # if (1st word, 2nd word) tuple exists in chains
        if ngram in chains:

            # find random next word by using previous two words as tuple and next word from values
            random_value_word = choice(chains[ngram])
            
            # add the random word to 'words' list
            words.append(random_value_word)

            # create empty list for reassigning tuples
            tuple_list = []

            # loop through index values for ngram tuple
            for i in range(len(ngram)):

                # if i is any index but the final index
                if i < len(ngram) - 1:

                    # reassign tuple value, move value by one
                    tuple_list.append(ngram[i+1])

                # if i is the final index value
                else:

                    # make last value in tuple the new word
                    tuple_list.append(random_value_word)
            
            # make a tuple out of the list
            ngram = tuple(tuple_list)
            
            # if last character of last word in ngram is a punctuation mark, randomly choose whether to break out of while loop
            if ngram[-1][-1] in (".", "?", "!"):
                x = randint(0,1)
                if x == 0:
                    break
        
        # else break out of loop
        else: 
            break

    return ' '.join(words)


# Open the file and turn it into one long string
input_text = open_and_read_file()

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)