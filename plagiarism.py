"""
Master file for running the entire project
"""
import re
import googletranslate.translate_shuffle_functions as tr

#Read in key
f = open('key.txt', 'r')
key = f.read()
f.close()

# Read in file
f = open('input/it_essay.txt', mode='r')
essay = f.read()
f.close()
# Split into sentences
sentences = re.compile("\.|\n").split(essay)

shuffledsentences = []
for sentence in sentences:
        sentence = tr.translateshuffle(sentence, 'en', 'de', key)
        shuffledsentences.append(sentence)

