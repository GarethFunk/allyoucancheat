from nltk.corpus import wordnet as wn
import inflect
p = inflect.engine()

def syn(word, code='NN'):
    # Decode the code
    pos = ""
    if code[0] == "N":
        try:
            if code[2] != "P":
                pos = wn.NOUN
        except IndexError:
            pass
    elif code[0] == "J":
        pos = wn.ADJ
    elif code[0] == "R":
        pos = wn.ADV
    elif code[0] == "V":
        pos = ""
    # If we managed to decode the code then do something
    if pos != "":
        synset = wn.synsets(word, pos)
        lemmata = []
        for syn in synset:
            for lem in syn.lemmas():
                lemmata.append({'name': lem.name(), 'count':lem.count(), 'syn':syn})
        # Pick a lemma somehow
        new_word = lemmata[0]['name']
    else:
        new_word = word
    return new_word


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
    words = []
    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            print(syn(word))

