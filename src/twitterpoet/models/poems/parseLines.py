import re, string
from rhymer.rhyme_checker import getPhone, isInDict, checkWeakRhyme
from syllables.sylla import syllables

ignored_words = re.compile(r'^[@#\\]|RT$|http://')
def parse(line):
    ''' Returns a dictionary of attributes ('syllables', 'phone') 
        note phone may be None, if the last word has no rhyme

        This ignores words like 'RT', '@foo', '#foo', 'http://..'
        ex. 'RT @someone: hello #friend :) #hi' -> 'hello :)'
    '''
    # List of words in line, ignores 'RT', '@foo', '#foo', emoji
    words = []
    for word in line.split( ):
        cleaned = re.sub('[\W_]+', '', word)
        if len(cleaned) != 0 and not ignored_words.findall(word):
            words.append(cleaned)
    if len(words) == 0:
        return {}
    # Remove ignored words from the actual tweet
    line = ' '.join([w for w in line.split() if not ignored_words.findall(w)])
    # words = filter(None, [re.sub('[\W_]+', '', word) for word in line.split( )])
    count = 0
    for word in words:
        count += syllables(word)
    phone = getPhone(words[-1])
    
    parsed = {'line':line, 'syllables':count, 'phone':phone}
    return parsed

if(__name__ == "__main__"):
    p1 = parse("hello i am hello")
    p2 = parse("but i was a yellow")
    if(checkWeakRhyme(p1['phone'], p2['phone'])):
        print "Win"
    else:
        print "Lose"
    print p1
    print p2

    while(True):
        line = raw_input('Line:')
        print parse(line)