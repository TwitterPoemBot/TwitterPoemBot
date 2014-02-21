import sys

#Rhymer class, used to determine if two words rhyme
class Rhymer:
    global rhy_dict
    rhy_dict = {}

    def __init__(self):
        f = open('CMU_Dict.txt', 'r')
        print f

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

    def isInDict(self, w):
        word = w.upper()
        return word in rhy_dict

    #method checks if two words rhymes
    def rhymes(self, w1, w2):
        word1 = w1.upper()
        word2 = w2.upper()
        if(self.isInDict(word1) and self.isInDict(word2)):
            #print rhy_dict[word1]
            #print rhy_dict[word2]
            return rhy_dict[word1] == rhy_dict[word2]
        else:
            print "Word(s) not in dictionary."
            return False


if(__name__ == "__main__"):
    r = Rhymer();

    while(True) :
        word1 = raw_input("Word 1: ")
        word2 = raw_input("Word 2: ")
        print r.rhymes(word1, word2)
