"""Define & Test Spelling Corrector using Levenshtein Distance.

Heather Qiu & Song Young Oh
September 2022

"""

import numpy as np

# 1. Define Levenshtein Distance Function
def calc_distance(w1, w2):
    if w1 == w2:
        return 0
    w1_len = len(w1)
    w2_len = len(w2)
    if w1 == "":
        return w2_len
    if w2 == "":
        return w1_len

    ## Create a Maxtrix (w1_len+1, w2_len+1)
    matrix = [[] for i in range(w1_len + 1)]
    for i in range(w1_len + 1):
        matrix[i] = [0 for j in range(w2_len + 1)]
    
    ## Initiate the first row and column
    for i in range(w1_len + 1):
        matrix[i][0] = i
    for j in range(w2_len + 1):
        matrix[0][j] = j
    
    ## Calculate the Distance
    for i in range(1, w1_len + 1):
        w1_character = w1[i - 1]
        for j in range(1, w2_len + 1):
            w2_character = w2[j - 1]
            cost = 0 if (w1_character == w2_character) else 1
            matrix[i][j] = min(
                [
                    matrix[i - 1][j] + 1,  # insertion
                    matrix[i][j - 1] + 1,  # deletion
                    matrix[i - 1][j - 1] + cost,  # substitution
                ]
            )
    return matrix[w1_len][w2_len]


# 2. Import the Provided Word List
word_list = np.loadtxt("https://norvig.com/ngrams/count_1w.txt", usecols=0, dtype=str)
list = word_list.copy()


# 3. Define Spelling Corrector Fuction
def spelling_corrector(input_word):
    sorted_list = sorted(
        list, key=lambda comparison_word: calc_distance(input_word, comparison_word)
    )
    print(sorted_list[0])


# 4. Test Spelling Corrector
test_cases = [
    "honsty",
    "pamily",
    "fredom",
    "amfibian",
    "countrary",
    "noticable",
    "mashine",
    "wonderfull",
    "beutiful",
    "devlopment",
    "sence",
    "griss",
    "johnedw",
    "jyv",
]

for test_word in test_cases:
    spelling_corrector(test_word)
