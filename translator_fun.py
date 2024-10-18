import pickle
import nltk
import TranslaterLogic

#Trigram pickle file contain the trigram model trained on Sinhala and Romanized Sinhala following the architeture of Ngram Model
translatorPic = open("trigramTrans.pickle", "rb")
translator = pickle.load(translatorPic)

        
# Code for creating trie
textFile = open("singlishtrain.txt",
                mode='r', encoding='utf-8')


#Main function to call the trigram structure
def triGramTranslate(sentence):
    sentence_romanized=sentence.split(" ")
    translation = ""
    translated = translator.tag(nltk.word_tokenize(sentence.lower()))
    #print(translated)
    i=-1
    for word, trans in translated:
        i+=1
        if trans in ('NNN'):
            translation = translation + str(TranslaterLogic.convertText(str(sentence_romanized[i])) + " ")
        else:
            translation = translation + str(trans + " ")
    return translation


#Suggestion Model Builder : Creating a trie structure

sData = []  # sinhala data tuple
eData = []  # english data tuple

lstword = []
final = []

def clearlstword():
    global lstword
    lstword = []


def translate(txt):
    clearlstword()
    if len(txt) >= 5:
        t.printAutoSuggestions(txt, 1)
    else:
        t.printAutoSuggestions(txt, 2)
    #print(lstword)
    return lstword


class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():

    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            sin_indexes = [n for n, x in enumerate(eData) if x == word]
            for i in sin_indexes:
                y = int(i)
                if sData[y] not in lstword:
                    # print(sData[y])
                    lstword.append(sData[y])

    def suggestionsRecsuffix(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            sin_indexes = [n for n, x in enumerate(eData) if x == word]
            for i in sin_indexes:
                y = int(i)
                if sData[y] not in lstword:
                    # print(sData[y])
                    lstword.append(sData[y])

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key, para):

        # adding text using rule
        # lstword.append(str(TranslaterLogic.convertText(key)))

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.

        node = self.root

        for a in key:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                return 0
            node = node.children[a]

        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not node.children:
            return -1
        if para == 1:
            self.suggestionsRecsuffix(node, key)
            return 1
        else:
            self.suggestionsRec(node, key)
            return 1

for i in textFile:
    txt = i.split("/")
    eData.append(txt[0])
    sData.append(txt[1].strip('\n'))

keys = eData
# keys to form the trie structure.
# creating trie object
t = Trie()
# creating the trie structure with the
t.formTrie(keys)
print("Tree generated")