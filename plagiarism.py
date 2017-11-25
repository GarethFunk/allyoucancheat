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
f = open('input/Emmas_essay.txt', mode='r')
essay = f.read()
f.close()

#Preprocessing
essay = essay.replace(".\"", "\".").replace("...", ".").replace("etc.", "etc").replace(" e.g.", ":").replace("i.e.", ":").replace("St.", "St")
essay = essay.replace("p.1", "p1").replace("p.2", "p2").replace("p.3", "p3").replace("p.4", "p4").replace("p.5", "p5").replace("p.6", "p6").replace("p.7", "p7").replace("p.8", "p8").replace("p.9", "p9")

# Split into sentences
sentences = re.compile("\.|\n").split(essay)

#Translate into french and back again
shuffledsentences = []
for sentence in sentences:
        sentence = tr.translateshuffle(sentence, 'en', 'de', key)
        shuffledsentences.append(sentence)
        print(sentence)

