import random

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
if __name__ != "__main__":
    import synon.patternInflect as pi
else:
    import patternInflect as pi

import inflection

def syn(word, code='NN'):
    wnl = WordNetLemmatizer()
    # Decode the code
    pos = ""
    if word[0].isupper() is False:
        # We dont want to look at proper nouns
        if code[0] == "N":
            try:
                if code[2] != "P":
                    # Not a proper noun
                    pos = wn.NOUN
            except IndexError:
                pos = wn.NOUN
            word = wnl.lemmatize(word, 'n')
        elif code[0] == "J":
            pos = wn.ADJ
            word = wnl.lemmatize(word, 'a') # Change it to the lemmatized form
        elif code[0] == "R":
            pos = wn.ADV
            word = wnl.lemmatize(word, 'r')
        elif code[0] == "V":
            pos = ""
    # If we managed to decode the code then do something
    if pos != "":
        print("Lemmatized word: " + word)
        synset = wn.synsets(word, pos)
        # Pick a lemma somehow
        lemma = __lemmaPicker(word, synset)
        print("Chosen new word: " + str(lemma))
        # Inflect the word again
        new_word = __inflector(lemma['name'], pos, code)
    else:
        new_word = word
    return new_word


def __inflector(word, pos, code):
    # Make human readable
    word = inflection.humanize(word)
    # This capitalises the first letter
    word = word.lower()
    if pos == wn.NOUN and code[-1] == "S":
        # This was a plural noun
        new_word = inflection.pluralize(word)
    elif pos == wn.ADV and code[-1] == "R":
        # Comparative adverb: faster
        new_word = pi.comparative(word) # These inflect just like adjectives
    elif pos == wn.ADV and code[-1] == "S":
        # Superlative adverb: fastest
        new_word = pi.superlative(word) # These inflect just like adjectives
    elif pos == wn.ADJ and code [-1] == "R":
        # Comparative adjective: prettier
        new_word = pi.comparative(word)
    elif pos == wn.ADJ and code[-1] == "S":
        # Superlative adjective: prettiest
        new_word = pi.superlative(word)
    else:
        new_word = word
    return new_word

def __lemmaPicker(word, synset):
    syn = __synsetPicker(word, synset)
    if syn is False:
        chosen_lemma = {'name':word, 'syn':""}
    else:
        # We got a synset so now pick a lemma from it
        lemmas = syn[0].lemmas()
        num = len(lemmas)
        total_count = 0
        for lem in lemmas:
            total_count += lem.count()
        if(total_count == 0):
            chosen_lemma = {'name':word, 'syn':syn}
        else:
            selecta = random.randint(1, total_count)
            run_tot = 0
            for lem in lemmas:
                run_tot += lem.count()
                if run_tot >= selecta:
                    # Choose this one
                    chosen_lemma =  {'name':lem.name(), 'syn':syn}
                    break
    return chosen_lemma


def __synsetPicker(word, synset):
    # Rank each synset by its count for the lemma we searched for
    synset_ranks = []
    for syn in synset:
        for lem in syn.lemmas():
            if lem.name() == word:
                synset_ranks.append((syn, lem.count()))
    if len(synset_ranks) == 0:
        chosen = False
    else:
        # Let's do some picking
        chosen = __mostPopular(synset_ranks)
        if chosen[1] == 0:
            # All the synsets had zero frequency
            chosen = False
    return chosen

def __mostPopular(synset_ranks):
    max_freq = -1
    for synset in synset_ranks:
        if synset[1] > max_freq:
            most_popular = synset
            max_freq = synset[1]
    return most_popular

def __scrub(word):
    # Remove punctuation and numbers
    punct_nums = [",", ".", "!", "@", "<", ">", "/", "?", "'", "\"", ":", ";", "|", "{", "}", "[", "]", "-", "_", "+", "=",
                  ")", "(", "*", "&", "^", "%", "$", "£", "#", "€", " ", "\n", "\t",
                  "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    new_word = ""
    for letter in word:
        if letter not in punct_nums:
            new_word += letter
    return new_word



if (__name__ == "__main__"):

    f = open('../input/it_essay.txt', mode='r')
    essay = f.read()
    f.close()
    # Split into sentences
    sentences = essay.split('.')
    nouns = ["dog", "dogs", "cat", "cats", "quickly", "quicker", "hard", "harder", "hardest", "good", "better", "prettiest",
             "well", "better"]
    codes = ["NN", "NNS", "NN", "NNS", "RB", "JJR", "RB", "RBR", "RBS", "JJ", "JJR", "JJS",
             "RB", "RBR"]
    nouns2 = ["ugly", "horrific", "quintessential", "salacious", "lewd", "undignified", "wanton"]
    codes2 = ["JJ", "JJ", "JJ", "JJ", "JJ", "JJ", "JJ"]
    for word, code in zip(nouns2, codes2):
        print(word + " -> " + syn(word, code) + "\n")

