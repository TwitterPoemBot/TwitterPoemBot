import re, string
from rhymer.rhyme_checker import getPhone, isInDict, checkWeakRhyme
from syllables.sylla import syllables

def parse(line):
    words = line.split( )
    sylla = 0
    for word in words:
        fixedWord = re.sub('[\W_]+', '', word)
        if(isInDict(fixedWord)):
            sylla += syllables(fixedWord)
            phone = getPhone(fixedWord)
        else:
            return {}
    
    parsed = {'line':line, 'syllables':sylla, 'phone':phone}
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
