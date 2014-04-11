import re, string, logging
from rhymer.rhyme_checker import getPhone, isInDict, checkWeakRhyme
from syllables.sylla import syllables
from sets import Set

# Words that will be filtered from the actual line of the tweetz
filtered_words = re.compile(r'^([@\\]|RT$)|https?://|www.')
# Words that won't be passed to syllable/rhymer
ignored_words = re.compile(r'[\W_]+')
non_english = re.compile(r'\\')

def is_english(line):
    ''' Returns if a line is in English 
        Line must be at least 30% english words,  60% roman characters
    '''
    w_threshold, c_threshold = 0.3, 0.6
    words = [w.strip(string.punctuation) for w in line.split()]
    word_count = len([w for w in words if isInDict(w)])
    char_count = len([c for c in line if ord(c) < 128])
    print [w for w in words if isInDict(w)]
    print [c for c in line if ord(c) < 128]
    return float(word_count) / len(words) >= w_threshold \
            and float(char_count) / len(line) >= c_threshold

def parse(line):
    ''' Parses an individual line '''

    line = line.replace('&amp', '&')    # Hardcoded rule for '&amp' to '&'
    logging.info("Parsing " + line)
    if not is_english(line):
        print "non-english: ", line
        print type(line)
        return {}
    # words is a list of the cleaned up words to feed syllable/rhymer
    words = []
    # line is the actual string of text to be presented to user
    for word in line.split( ):
        cleaned = re.sub('[\W_]+', '', word) # Remove punctuation
        if len(cleaned) != 0 and not filtered_words.findall(word):
            words.append(cleaned)
    if len(words) == 0:
        return {}
    # Remove hashtags at the end from the line
    while (words[-1][0] == '#'):
        words.pop(-1)
    # Remove ignored words from the actual tweet
    line = ' '.join([w for w in line.split() if not filtered_words.findall(w)])
    # words = filter(None, [re.sub('[\W_]+', '', word) for word in line.split( )])
    line = re.sub(r'#', '', line)
    count = 0
    for word in words:
        count += syllables(word)
    phone = getPhone(words[-1])
    last_word = words[-1].lower();
    
    parsed = {'line':line, 'syllables':count, 'phone':phone, 'last_word':last_word, 'url':""}
    logging.info(parsed)
    return parsed

def parse_all(tweets):
    ''' Returns a unique list of dictionaries with keys ('line', syllables', 'phone') 
        given a list of tweets and their urls (ex. ['tweet 1', 'url 1', 'tweet 2', 'url 2'])
        note 'phone' may be None, if the last word has no rhyme.

        This ignores words like 'RT', '@foo', '#foo', 'http://..'
        ex. 'RT @someone: hello #friend :) #hi' -> 'hello :)'
    '''
    urls = tweets[1::2]
    tweets = tweets[0::2]

    seen_tweets = {} # For avoiding duplicate tweets
    parsed_tweets = [] # The list of dictionaries to return
    count, rejected, duplicates = 0, 0, 0 # For logging purposes
    for tweet in tweets:
        parsed = parse(tweet) 
        # Reject if parsed fails or if the cleaned tweet text is duplicated
        if parsed == {}:
            rejected += 1
        elif seen_tweets.get(parsed['line']):
            duplicates += 1
        else:
            parsed['url'] = urls.pop(0)
            parsed_tweets.append(parsed)
            seen_tweets[parsed['line']] = 1
        count += 1
    # parsed_tweets = [parse(tweet) for tweet in tweets if parse(tweet) != {}]
    logging.info('Total tweets:' +  str(count) + ' rejected:' + str(rejected) + ' duplicates:' + str(duplicates))
    return parsed_tweets

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
