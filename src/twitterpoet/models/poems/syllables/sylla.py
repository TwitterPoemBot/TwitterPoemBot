import re, os, sys
import logging
dictionaries=['mhyph.txt']
dicts = []
vowel = re.compile(r'([aoiuy]|ee)+')
digit = re.compile(r'\d')

# Set-up
try:
    f = open(os.path.join(os.path.dirname(__file__), os.pardir, 'CMU_Dict.txt'), 'r')
except:
    f = open(os.path.join(os.pardir, 'CMU_Dict.txt'), 'r')
syllable_dic = {}
for line in f:
    if(line.find(';;;') != -1):
        continue
    words = line.split()
    word = words[0].lower()
    syllable_count = sorted([len([p for p in words[1:] if digit.search(p)])])
    if word[-1] == ')':
        syllable_dic[word[:-3]] += syllable_count
    else:
        syllable_dic[word] = syllable_count
f.close()

def syllables(word):
    ''' Returns the number of syllables in the given word '''
    word = word.lower()
    # Ignore URLs, hashtags, usernames
    if len(word) == 0 or word[:4] == 'http' or word[0] in ['#', '@']:
        return 0
    if word in syllable_dic:
        return syllable_dic[word][0]
    # Handle numbers
    # Use heuristic if it's not in any dictionary
    # logging.warning('Using heuristic')
    if len(word) <= 3:
        return 1
    else:
        count = len(vowel.findall(word))
    if word[-1] == 'e' and not vowel.findall(word[-2]) and vowel.findall(word[-3]):
        count -= 1
    return count

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
    while(True) :
        word1 = raw_input("Word: ")
        print syllables(word1)





