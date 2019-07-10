import pprint as pp
import re
import time

'''
Google search-influenced algorithm
finds Googled "results" (sentences) using keywords
this code uses sentences from text files to emulate results
dictionary-based, so should be fast, but needs to be compared to faster search algorithms than O(n)
using large text file to ~hopefully~ see how fast it actually runs
idea came from how Google apparently does its own searches
'''

# for removing unnecessary characters from items in a list
# useful for creating a more accurate dictionary
# INPUTS: list of strings, character to strip
# OUTPUT: list of strings
def parser(sentence, remove):
    my_list = []
    for word in sentence:
        my_list.append(word.strip(remove))
    return my_list

# slow search algorithm to compare results of our search algorithm
# O(n) speed
# currently only works for one searched word, but easy to correct
def O_n_comparision():
    with open('bible10.txt', 'r') as fp:
        text = fp.read()
        text = text.split()

        t0 = time.time()
        count = 0
        # goes through each individual word of the entire text file
        for word in text:
            if word == 'the':
                count += 1
        t1 = time.time()
        print(t1 - t0)
        print(count)


# issue with "Mr. Mrs. etc"
def main():
    # dictionary key: single word in a sentence ... value: list of all sentences with that word
    my_dict = {}
    with open('bible10.txt', 'r') as fp:
        text = fp.read()
        # converting newline to space
        sentences = re.sub('\n', ' ', text)
        sentences = sentences.split('. ')

        #going through all words in all sentences to create a dictionary with keys of every word
        for sentence in sentences:
            word_list = sentence.split()
            for word in word_list:
                # adding sentence to dictionary
                if word in my_dict.keys():
                    my_dict[word].append(sentence)
                else:
                    my_dict[word] = []
                    my_dict[word].append(sentence)

    # start time of search
    t0 = time.time()
    # word being searched
    search = 'the'

    search_list = search.split()
    # combined list of all sentences with the searched word in them
    comb_list = []
    for word in search_list:
        if word in my_dict.keys():
            if not comb_list:
                comb_list = my_dict[word]
            else:
                # filtering out sentences that are not in both list values
                comb_list = list(set(comb_list) & set(my_dict[word]))

    t1 = time.time()
    print(t1 - t0)
    print(len(comb_list))



if __name__ == '__main__':
    main()