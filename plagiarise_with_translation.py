import re
import googletranslate.translate_shuffle_functions as tr

# Read in key.txt
f = open('key.txt', 'r')
key = f.read()
f.close()

def refactor(essay):

    return essay

def plagiarise_with_translation(essay):

    global key

    #Preprocessing
    essay = essay.replace(".\"", "\".").replace("...", ".").replace("etc.", "etc").replace(" e.g.", ":").replace("i.e.", ":").replace("St.", "St")
    essay = essay.replace("p.1", "p1").replace("p.2", "p2").replace("p.3", "p3").replace("p.4", "p4").replace("p.5", "p5").replace("p.6", "p6").replace("p.7", "p7").replace("p.8", "p8").replace("p.9", "p9")

    trans_essay = tr.translateshuffle(essay, 'en', 'fr', key, 'nmt');
    return refactor(trans_essay)

if (__name__ == "__main__"):
    #read in file
    f = open('input/Emmas_essay.txt', mode='r')
    essay = f.read()
    f.close()
    shuffledessay = plagiarise_with_translation(essay)
    print(shuffledessay)