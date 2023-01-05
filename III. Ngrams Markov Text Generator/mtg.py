"""Markov Text Generator.

Heather Qiu
September 2022

"""

import copy
import numpy as np

# a function that goes through all ngram tokens in a corpus and count the number of times each token appears
def get_ngram_counts(n, corpus):
    ngram_counts = {}
    for i in range(len(corpus) - n + 1):
        ngram = tuple(corpus[i : i + n])
        if ngram in ngram_counts.keys():
            ngram_counts[ngram] += 1
        else:
            ngram_counts[ngram] = 1
    return ngram_counts


# a function that calculates the probabilities of a word appearing after a prefix.
# If a higher-order n-gram has a zero count, we simply backoff to a lower order n-gram.
# If deterministic flag is true, then return the word with the highest probabilities of appearing after a prefix.
# Otherwise (i.e. stochastic mode), return the randomly chosen word from all probable options.
def get_next_word(sentence, n, corpus, deterministic):

    new_sentence = list()
    corpus_probabilities = {}
    ngramcount_numerator = get_ngram_counts(n, corpus)
    ngramcount_denominator = get_ngram_counts(n - 1, corpus)
    last_ngram = sentence[1 - n :]
    denominator_count = ngramcount_denominator.get(tuple(last_ngram), 0)
    if denominator_count == 0:
        # backoff
        sentence_copy = copy.deepcopy(sentence)
        beginning_sentence = sentence_copy[:1]
        backoff_sentence = get_next_word(sentence[1:], n - 1, corpus, deterministic)
        new_sentence = beginning_sentence + backoff_sentence

    else:
        vocab = set(corpus)
        for w in vocab:
            l_ngram = copy.deepcopy(last_ngram)
            l_ngram.append(w)
            numerator_count = ngramcount_numerator.get(tuple(l_ngram), 0)
            probability = numerator_count / denominator_count
            corpus_probabilities[w] = probability

        # deterministic vs. stochastic modes
        if deterministic == True:
            suggestions_t = sorted(
                corpus_probabilities.items(), key=lambda x: x[1], reverse=True
            )[:1]
            new_sentence = copy.deepcopy(sentence)
            new_sentence.append(suggestions_t[0][0])
        else:
            suggestions_f = np.random.choice(list(corpus_probabilities.keys()))
            new_sentence = copy.deepcopy(sentence)
            new_sentence.append(str(suggestions_f))
    return new_sentence


# a function that calls get_next_word() function and returns an extended sentence
# until the first ., ?, or ! is found OR until it has 10 total tokens.
def finish_sentence(sentence, n, corpus, deterministic=False):
    s = copy.deepcopy(sentence)
    while len(s) < 10:
        s = get_next_word(s, n, corpus, deterministic)
        if "." in s or "?" in s or "!" in s:
            break
    return s
