import re, string, logging
from rhymer.rhyme_checker import getPhone, isInDict, checkWeakRhyme
from syllables.sylla import syllables
from sets import Set

ignored_words = re.compile(r'^[@\\]|RT$|https?://|www.')
# end_hashtags = re.compile(r'(#\S*\b)+$')

def parse(line):
    ''' Parses an individual line ''' 
    # List of words in line, ignores 'RT', '@foo', '#foo', emoji
    words = []
    for word in line.split( ):
        cleaned = re.sub('[\W_]+', '', word)
        if len(cleaned) != 0 and not ignored_words.findall(word):
            words.append(cleaned)
    if len(words) == 0:
        return {}
    # Remove hashtags at the end from the line
    while (words[-1][0] == '#'):
        words.pop(-1)
    # Remove ignored words from the actual tweet
    line = ' '.join([w for w in line.split() if not ignored_words.findall(w)])
    # words = filter(None, [re.sub('[\W_]+', '', word) for word in line.split( )])
    line = re.sub(r'#', '', line)
    count = 0
    for word in words:
        count += syllables(word)
    phone = getPhone(words[-1])
    last_word = words[-1];
    
    parsed = {'line':line, 'syllables':count, 'phone':phone, 'last_word':last_word}
    return parsed

def parse_all(tweets):
    ''' Returns a unique list of dictionaries with keys ('line', syllables', 'phone') 
        note 'phone' may be None, if the last word has no rhyme.

        This ignores words like 'RT', '@foo', '#foo', 'http://..'
        ex. 'RT @someone: hello #friend :) #hi' -> 'hello :)'
    '''

    seen_tweets = {} # For avoiding duplicate tweets
    parsed_tweets = [] # The list of dictionaries to return
    count, rejected, duplicates = 0, 0, 0 # For logging purposes
    for tweet in tweets:
        logging.info(tweet)
        parsed = parse(tweet) 
        # Reject if parsed fails or if the cleaned tweet text is duplicated
        if parsed == {}:
            rejected += 1
        elif seen_tweets.get(parsed['line']):
            duplicates += 1
        else:
            parsed_tweets.append(parsed)
            seen_tweets[parsed['line']] = 1
        count += 1
    # parsed_tweets = [parse(tweet) for tweet in tweets if parse(tweet) != {}]
    print '-----'
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
    print parse_all(['hello', 'hello', 'jello'])
    while(True):
        line = raw_input('Line:')
        print parse(line)
