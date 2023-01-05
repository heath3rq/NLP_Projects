""" Generate the components of a part-of-speech hidden markov model. 

Heather Qiu & Song Young Oh
October 2022

"""

import nltk
import numpy as np
from POS_viterbi import (
    viterbi,
)  ## you will need place the current file in the same folder as the viterbi function

corpus = nltk.corpus.brown.tagged_sents(tagset="universal")[:10000]

sentences, pos_tags = [], []
for sentence in corpus:
    for word in sentence:
        sentences.append(word[0])
        pos_tags.append(word[1])

states = list(set(pos_tags))
words = list(set(sentences))
words.append("UNK")

## Build Transition Matrix
transition_matrix = np.ones((len(states), len(states)))
for sentence in corpus:
    for index in range(1, len(sentence)):
        prev_state = sentence[index - 1][1]
        current_state = sentence[index][1]
        i = states.index(prev_state)
        j = states.index(current_state)
        transition_matrix[i][j] = transition_matrix[i][j] + 1

# sum_of_states_rows = transition_matrix.sum(axis=1)
# A = transition_matrix / sum_of_states_rows

## Build Emission Matrix
emission_matrix = np.ones((len(states), len(words)))
for sentence in corpus:
    for index in range(0, len(sentence)):
        current_word = sentence[index][0]
        current_state = sentence[index][1]
        i = states.index(current_state)
        j = words.index(current_word)
        emission_matrix[i][j] = emission_matrix[i][j] + 1

# sum_of_states_col = emission_matrix.sum(axis=0)
# B = emission_matrix / sum_of_states_col

## Build Initial Probability Distribution
pi_matrix = np.ones((len(states)))
for sentence in corpus:
    init_state = states.index(sentence[0][1])
    pi_matrix[init_state] = pi_matrix[init_state] + 1


## Test Cases
test_sentences = nltk.corpus.brown.tagged_sents(tagset="universal")[10150:10153]
for sentence in test_sentences:
    input = []
    for word in sentence:
        # print(word)
        if word[0] in words:
            word_index = words.index(word[0])
            input.append(word_index)
        else:
            word_index = words.index("UNK")  #'UNK' word
            input.append(word_index)
    print(sentence)
    input_word_state_indices, _ = viterbi(
        input, pi_matrix, transition_matrix, emission_matrix
    )
    output_states = [states[state] for state in input_word_state_indices]
    print(f"The corresponding states from my POS tagger are {output_states}.")
    print(
        "############################ TEST CASE SEPERATOR ############################"
    )
