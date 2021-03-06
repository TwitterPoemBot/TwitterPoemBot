import sys
import os

rhy_dict = {}
try:
    f = open(os.path.join(os.path.dirname(__file__), os.pardir, 'CMU_Dict.txt'), 'r')
except:
    f = open(os.path.join(os.pardir, 'CMU_Dict.txt'), 'r')
    
for line in f:
    if(line.find(';;;') == -1):
        parts = line.split( )
        i = -1
        while (not (any(char.isdigit() for char in parts[i]))):
            i = i - 1
            if(i <= -1 * len(parts)):
                break
        end = ""
        for x in range(i, 0):
            end += parts[x]
        rhy_dict[parts[0]] = end

def isInDict(w):
    word = w.upper()
    return word in rhy_dict

def getPhone(w):
    word = w.upper()
    try:
        return rhy_dict[word]
    except:
        return None

def checkWeakRhyme(a1, a2):
    ''' Check if two words rhyme weakly '''
    weak = {'AA':1, 'AE':2, 'AH':3, 'AO':1, 'AW':5, 'AY':6, 'EH':7, 'ER':8,
                'EY':9, 'IH':10, 'IY':11, 'OW':12, 'OY':13, 'UH':14, 'UW':15}
    return (weak[a1[:2]] == weak[a2[:2]]) and (a1[3:] == a2[3:])

def rhymes(w1, w2):
    ''' Checks if two words rhyme '''
    word1 = w1.upper()
    word2 = w2.upper()
    if(isInDict(word1) and isInDict(word2)):
        return rhy_dict[word1] == rhy_dict[word2]
    else:
        print "Word(s) not in dictionary."
        return False


if(__name__ == "__main__"):
    while(True) :
        word1 = raw_input("Word 1: ")
        word2 = raw_input("Word 2: ")
        print rhymes(word1, word2)
        print getPhone(word1)
        print getPhone(word2)

