import re
import googletranslate.translate_shuffle_functions as tr

# Read in key.txt
from grammarmunger.parser import paraphrase_with_structure_maps

f = open('key.txt', 'r')
key = f.read()
f.close()

def refactor(essay):
    # Dissect. Split up into sentences  but preserve the paragraphing
    # break down the sentences into a tuple with ("sentence", "trailing whitespace")
    # and assemble these into a list
    splts = re.split("([\.?!]\s+)", essay)
    sentences = []
    for first, second in zip(splts[0::2], splts[1::2]):
        sentences.append([first, second])
    # Handle the final one - dont care if we loose whitespace here.
    sentences.append([splts[-1], ""])
    # Do something with the sentences
    for sentence in sentences:
        sentence[0] = paraphrase_with_structure_maps(sentence[0])

    # Reassemble
    new_essay = ""
    for sentence in sentences:
        new_essay += sentence[0]
        new_essay += sentence[1]
    return new_essay

def plagiarise_with_translation(essay):

    global key

    #Preprocessing
    essay = essay.replace(".\"", "\".").replace("...", ".").replace("etc.", "etc").replace(" e.g.", ":").replace("i.e.", ":").replace("St.", "St")
    essay = essay.replace("p.1", "p1").replace("p.2", "p2").replace("p.3", "p3").replace("p.4", "p4").replace("p.5", "p5").replace("p.6", "p6").replace("p.7", "p7").replace("p.8", "p8").replace("p.9", "p9")

    trans_essay = tr.translateshuffle(essay, 'en', 'fr', key, 'nmt');
    return refactor(trans_essay)

if (__name__ == "__main__"):
    #read in file
    f = open('input/it_essay.txt', mode='r')
    essay = f.read()
    f.close()
    #shuffledessay = plagiarise_with_translation(essay)
    refactor(essay)