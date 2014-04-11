from random import sample
import logging

def limerick(corpus):
    ''' Generates a limerick given a dictionary of line/syllables/phone ''' 

    def get_lines(sylla_min, sylla_max, n):
        ''' Returns dic of at least n rhyming tweets within the given syllable range
            ex. {'ha1':['some tweet text', 'some other text']} '''

        lines = [line for line in corpus if line['syllables'] >= sylla_min and line['syllables'] <= sylla_max] 
        dic = {}
        # dic is a dictionary of phone strings to line dictionaries
        for line in lines:
            phone = line['phone']
            if phone is None:
                continue
            elif phone in dic:
                # Avoid repeated last words
                if line['last_word'] not in [l['last_word'] for l in dic[phone]]:
                    dic[phone].append(line)
            else:
                dic[phone] = [line]
        # Pick the least syllabically variant n lines
        return_lines = ''
        least_variance = 999
        for key in dic:
            lines = dic[key]
            if len(lines) >= n:
                # Check variance, we want lines with similar syllable counts
                variance = max(lines, key=lambda line:line['syllables'])['syllables'] - \
                           min(lines, key=lambda line:line['syllables'])['syllables']

                if len(return_lines) == 0 or least_variance > variance:
                    return_lines = [line['line'] for line in lines]
                    least_variance = variance
                    logging.info("best lines: ")
                    logging.info(return_lines)
        if len(return_lines) != 0:
            return return_lines
        else:
            raise ValueError

    '''
    6-12A
    6-12A
    3-6B
    3-6B
    6-10A
    '''
    try:
        a = get_lines(6, 12, 3) # Get 3 6-10 syllable lines that rhyme
        b = get_lines(3, 6, 2)  # Get 2 3-6 syllable lines that rhyme
    except ValueError as e:
        raise Exception('Could not construct limerick - not enough tweets') 
    print "Limerick: A, B"
    print a
    print b
    poem = a[:2]
    poem += b
    poem += a[2:3]
    return '\n'.join(poem)


