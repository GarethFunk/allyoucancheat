import re
import googletranslate.translate_shuffle_functions as tr

def plagiarise_with_translation(essay):

    #Read in key.txt
    f = open('key.txt', 'r')
    key = f.read()
    f.close()

    #Preprocessing
    essay = essay.replace(".\"", "\".").replace("...", ".").replace("etc.", "etc").replace(" e.g.", ":").replace("i.e.", ":").replace("St.", "St")
    essay = essay.replace("p.1", "p1").replace("p.2", "p2").replace("p.3", "p3").replace("p.4", "p4").replace("p.5", "p5").replace("p.6", "p6").replace("p.7", "p7").replace("p.8", "p8").replace("p.9", "p9")

    # Split into sentences
    sentences = re.compile("\.|\n").split(essay)

    #Translate into french and back again

    shuffledsentences = []
    for sentence in sentences:
        sentence = tr.translateshuffle(sentence, 'en', 'fr', key, 'nmt')
        shuffledsentences.append(sentence)

        '''
    #Translate into multiple languages
    shuffledsentences = []
    for sentence in sentences:
        sentence = tr.translateshuffleflexible(sentence, 'en', 'ru', 'es', 'fr', key, 'base', 'nmt')
        shuffledsentences.append(sentence)
        print(sentence)
    '''
    return shuffledsentences

if (__name__ == "__main__"):
    #read in file
    f = open('input/Emmas_essay.txt', mode='r')
    essay = f.read()
    f.close()
    shuffledessay = plagiarise_with_translation(essay)
    print(shuffledessay)